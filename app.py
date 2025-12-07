from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

MEME_FOLDER = "static/memes"
os.makedirs(MEME_FOLDER, exist_ok=True)


def draw_text_with_outline(draw, text, position, font):
    if not text:
        return

    text = text.upper()
    x, y = position
    thickness = max(2, font.size // 15)

    for dx in range(-thickness, thickness + 1):
        for dy in range(-thickness, thickness + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill="black", anchor="mm")

    draw.text((x, y), text, font=font, fill="white", anchor="mm")


@app.route("/", methods=["GET", "POST"])
def index():
    meme_path = None

    if request.method == "POST":
        image = request.files.get("image")
        top_text = request.form.get("top_text", "")
        bottom_text = request.form.get("bottom_text", "")

        if image:
            img = Image.open(image.stream).convert("RGB")
            draw = ImageDraw.Draw(img)
            w, h = img.size

            font_size = int(w / 7)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except OSError:
                font = ImageFont.load_default()

            top_position = (w / 2, h * 0.15)
            bottom_position = (w / 2, h * 0.85)

            draw_text_with_outline(draw, top_text, top_position, font)
            draw_text_with_outline(draw, bottom_text, bottom_position, font)

            output_path = os.path.join(MEME_FOLDER, "generated_meme.jpg")
            img.save(output_path)
            meme_path = output_path

    return render_template("index.html", meme_path=meme_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

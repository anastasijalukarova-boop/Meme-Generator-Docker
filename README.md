# Meme Generator (Docker)

Preprosta Flask aplikacija, ki omogoča nalaganje slike, vnos zgornjega in spodnjega teksta ter generiranje meme slike. Projekt je dockeriziran, tako da se aplikacija zaganja znotraj Docker kontejnerja.

## Uporabljene tehnologije

- Python
- Flask
- Pillow
- Docker

## Zagon z Dockerjem

```bash
docker build -t meme-generator .
docker run -p 5000:5000 meme-generator

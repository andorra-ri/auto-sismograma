# Sismes

Instal·lar [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) i [docker](https://docs.docker.com/engine/install/) pel sistema operatiu corresponent

Clonar el repositori i fer un build de la imatge

```bash
git clone https://github.com/andorra-ri/auto-sismograma.git
cd auto-sismograma
docker build .
```

Aixecar el contenidor Docket amb l'aplicació per generar el sismograma en en el moment actual amb finestra mòvil de 24h.

```bash
docker compose up

# Rebuild de la imatge si s'ha fet algun canvi
# docker compose up --build
```

## Agraïments

Aquest script s'inspira en un utilitzat per l'ICGC (Institut Cartogràfic i Geològic de Catalunya). Tot i que el nostre projecte ha evolucionat de manera independent, la seva feina ha establert les bases per a certs aspectes.

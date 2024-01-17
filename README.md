# Sismes

Instal·lar [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) i [docker](https://docs.docker.com/engine/install/) pel sistema operatiu corresponent

Clonar el repositori

```bash
git clone https://github.com/andorra-ri/auto-sismograma.git
cd auto-sismograma
```

Ajustar (si cal) el fitxer `cronfile` per executar el sismograma periòdicament. [Crontab Guru](https://crontab.guru/#*/5_*_*_*_*)

Crear un fitxer `.env` dins el directori `src` amb la configuració de Supabase.

```env
SUPABASE_ID=
SUPABASE_TOKEN=
```

Aixecar el contenidor Docker amb l'aplicació en mode detached. El contenidor quedarà actiu i executarà el sismograma en funció de la calendarització definida al cronfile.

```bash
docker compose up -d

# Rebuild de la imatge si s'ha fet algun canvi o si és la primera vegada que s'exeuta
# docker compose up -d --build
```

## Agraïments

Aquest script s'inspira en un utilitzat per l'ICGC (Institut Cartogràfic i Geològic de Catalunya). Tot i que el nostre projecte ha evolucionat de manera independent, la seva feina ha establert les bases per a certs aspectes.

# Sismes

## Execució automàtica en Google Cloud

Actualment, el projecte s’executa de manera automàtica a Google Cloud.
Cada vegada que es fa un commit a la branca `main`, els canvis es construeixen i es despleguen automàticament a producció.
Això garanteix que el servei estigui sempre executant l’última versió del codi.

Instal·lar [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) i [docker](https://docs.docker.com/engine/install/) pel sistema operatiu corresponent

---

## Execució en local (opcional)

Si es vol executar el projecte en local per desenvolupament o proves, es pot fer de dues maneres:

### Opció 1: Utilitzant Docker (Dockerfile)

Instal·lar [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) i [docker](https://docs.docker.com/engine/install/) pel sistema operatiu corresponent

Clonar el repositori:

```bash
git clone https://github.com/andorra-ri/auto-sismograma.git
cd auto-sismograma
```

Crear un fitxer .env dins el directori src amb la configuració de Supabase:
```bash
SUPABASE_ID=
SUPABASE_TOKEN=
```

Construir la imatge Docker a partir del `Dockerfile`:
```bash
docker build -t auto-sismograma .
```

Executar el contenidor:
```bash
docker run -d --env-file src/.env auto-sismograma
```

### Opció 2: Execució directa amb entorn virtual (.venv)

Crear un entorn virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
# .venv\Scripts\activate   # Windows
```

Instal·lar les dependències:
```bash
pip install -r requirements.txt
```

Crear el fitxer .env dins src amb les credencials necessàries:
```bash
SUPABASE_ID=
SUPABASE_TOKEN=
```

Executar el fitxer principal de l’aplicació:
```bash
python src/main.py
```

---

## Agraïments

Aquest script s'inspira en un utilitzat per l'ICGC (Institut Cartogràfic i Geològic de Catalunya). Tot i que el nostre projecte ha evolucionat de manera independent, la seva feina ha establert les bases per a certs aspectes.

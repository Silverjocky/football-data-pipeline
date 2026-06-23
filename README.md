# Football Data Pipeline 🏟️

Pipeline ETL que extrae datos de partidos de La Liga española desde la API de football-data.org, los transforma y los carga en AWS S3.

## Arquitectura

API football-data.org → Extract → Transform → Load → AWS S3

## Tecnologías

- **Python** — Lenguaje principal
- **Pandas** — Transformación de datos
- **Boto3** — Conexión con AWS S3
- **AWS S3** — Almacenamiento en la nube

## Estructura del proyecto

football-data-pipeline/

├── src/

│   ├── extract.py      # Extrae datos de la API

│   ├── transform.py    # Limpia y transforma los datos

│   └── load.py         # Sube los datos a AWS S3

├── data/               # Archivos generados localmente

├── .env.example        # Variables de entorno requeridas

├── main.py             # Orquestador del pipeline

└── requirements.txt    # Dependencias del proyecto

## Datos extraídos

380 partidos de La Liga española con los siguientes campos:

- `match_id`, `date`, `matchday`, `status`
- `home_team`, `away_team`, `winner`
- `home_goals`, `away_goals`
- `year`, `month` — extraídos de la fecha

## Almacenamiento en S3

football-data-pipeline-stm1312/

├── raw/

│   └── matches.csv                      # Datos crudos

└── processed/

├── matches_transformed.csv          # Datos transformados

└── matches_transformed.parquet      # Formato optimizado

## Cómo ejecutarlo

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/football-data-pipeline.git
cd football-data-pipeline
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Edita .env con tu API Key de football-data.org
```

### 5. Configurar AWS
```bash
aws configure
```

### 6. Ejecutar el pipeline
```bash
python main.py
```
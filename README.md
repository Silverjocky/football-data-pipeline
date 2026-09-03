# Football Data Pipeline 🏟️

Pipeline ETL que extrae datos de partidos de La Liga española desde la API de football-data.org, los transforma y los carga en AWS S3, catalogados con AWS Glue y consultables con Amazon Athena.

## Arquitectura

API football-data.org → Extract → Transform → Load → AWS S3 → AWS Glue (Crawler) → Amazon Athena

## Tecnologías

- **Python** — Lenguaje principal
- **Pandas** — Transformación de datos
- **PyArrow** — Escritura de Parquet particionado
- **Boto3** — Conexión con AWS S3
- **AWS S3** — Almacenamiento en la nube
- **AWS Glue** — Catalogación de esquemas y particiones (Data Catalog)
- **Amazon Athena** — Consultas SQL serverless sobre los datos en S3

## Estructura del proyecto

football-data-pipeline/

├── src/

│   ├── extract.py      # Extrae datos de la API

│   ├── transform.py    # Limpia, transforma y particiona los datos

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
- `year`, `month` — extraídos de la fecha (también usados como claves de partición)

> Nota: la API incluye tanto partidos ya jugados como calendario a futuro, por lo que el dataset puede contener fechas de temporadas próximas.

## Almacenamiento en S3

football-data-pipeline-stm1312/

├── raw/

│   └── matches.csv                            # Datos crudos

└── processed/

├── matches_transformed.csv                # Datos transformados, sin particionar

└── matches_transformed_partitioned/       # Datos transformados en Parquet, particionados

├── year=2026/month=9/*.parquet

└── year=.../month=.../*.parquet

## Catalogación y consultas (AWS Glue + Athena)

- Un **Glue Crawler** apunta al prefijo `processed/matches_transformed_partitioned/`, detecta el esquema automáticamente y registra `year` y `month` como claves de partición en el Data Catalog.
- Los datos son consultables directamente con **Amazon Athena** sin necesidad de una base de datos tradicional. Filtrar por partición (`WHERE year = '2026' AND month = '9'`) reduce significativamente el volumen de datos escaneado por consulta, y por lo tanto el costo.

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

### 7. Catalogar y consultar (opcional, requiere consola de AWS)
1. Crea un Glue Crawler apuntando a `s3://football-data-pipeline-stm1312/processed/matches_transformed_partitioned/`.
2. Ejecútalo para generar la tabla en el Data Catalog.
3. Consulta los datos desde Amazon Athena usando la base de datos generada.
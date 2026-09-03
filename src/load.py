import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# Conectarse a S3
s3 = boto3.client("s3")

# Variables
BUCKET_NAME = "football-data-pipeline-stm1312"

# Archivos a subir
files = [
    ("data/matches.csv",                "raw/matches.csv"),
    ("data/matches_transformed.csv",    "processed/matches_transformed.csv"),
]

# Subir archivos
for local_file, s3_key in files:
    s3.upload_file(local_file, BUCKET_NAME, s3_key)
    print(f"Subido: s3://{BUCKET_NAME}/{s3_key}")
    
# Dataset particionado conservando year=/mont=/
PARTITIONED_LOCAL_DIR = "data/processed_partitioned"
PARTITIONED_S3_PREFIX = "processed/matches_transformed_partitioned"
 
for root, _, filenames in os.walk(PARTITIONED_LOCAL_DIR):
    for filename in filenames:
        local_path = os.path.join(root, filename)
        # ruta relativa dentro de processed_partitioned, ej: year=2026/month=9/archivo.parquet
        relative_path = os.path.relpath(local_path, PARTITIONED_LOCAL_DIR)
        s3_key = f"{PARTITIONED_S3_PREFIX}/{relative_path}".replace("\\", "/")
        s3.upload_file(local_path, BUCKET_NAME, s3_key)
        print(f"Subido: s3://{BUCKET_NAME}/{s3_key}")
    

print("\n¡Carga completada!")
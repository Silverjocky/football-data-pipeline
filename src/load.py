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
    ("data/matches_transformed.parquet","processed/matches_transformed.parquet")
]

# Subir archivos
for local_file, s3_key in files:
    s3.upload_file(local_file, BUCKET_NAME, s3_key)
    print(f"Subido: s3://{BUCKET_NAME}/{s3_key}")
    

print("\n¡Carga completada!")
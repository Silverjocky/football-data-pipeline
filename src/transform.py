import pandas as pd

df = pd.read_csv("data/matches.csv")

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

print("Datos cargados: ")
print(df.info())
print(df["date"].head())

print(df.describe())

print(df["winner"].value_counts())

print(df[["date", "year", "month"]].head())

df.to_csv("data/matches_transformed.csv", index=False)

print("CSV generado correctamente")

df.to_parquet("data/matches_transformed.parquet", index=False)
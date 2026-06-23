import os
import requests
from dotenv import load_dotenv
from pprint import pprint
import pandas as pd

load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")

headers = {
    "X-Auth-Token": API_KEY
}

url = "https://api.football-data.org/v4/competitions/PD/matches"

response = requests.get(url, headers=headers)

data = response.json()

print("Tipo de data:")
print(type(data))

print("\nLlaves principales:")
print(data.keys())

matches = data["matches"]

match = matches[0]



from pprint import pprint


records = []

for match in matches:
    record = {
    "match_id": match["id"],
    "date": match["utcDate"],
    "season_id": match["season"]["id"],
    "matchday": match["matchday"],
    "status": match["status"],
    "home_team_id": match["homeTeam"]["id"],
    "home_team": match["homeTeam"]["name"],
    "away_team_id": match["awayTeam"]["id"],
    "away_team": match["awayTeam"]["name"],
    "winner": match["score"]["winner"],
    "home_goals": match["score"]["fullTime"]["home"],
    "away_goals": match["score"]["fullTime"]["away"]
    }
    records.append(record)

print(f"\nTotal de registros {len(records)}")

df = pd.DataFrame(records)

print(df.head())

print(df.info())

df["date"] = pd.to_datetime(df["date"])
print(df["date"].dtype)
print(df.head())

print("\nCantidad de nulos: ")
print(df.isnull().sum())

print(df["winner"].unique())
print(df["home_goals"].unique())

df.to_csv("data/matches.csv", index=False)
print("Archivo guardado correctamente")
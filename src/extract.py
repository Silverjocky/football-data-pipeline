import os
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")
API_URL = "https://api.football-data.org/v4/competitions/PD/matches"


def fetch_matches():
    headers = {"X-Auth-Token": API_KEY}
    try:
        response = requests.get(API_URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API de football-data.org: {e}")
        raise

    return response.json()


def parse_matches(data):
    matches = data["matches"]
    records = []
    for match in matches:
        records.append({
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
            "away_goals": match["score"]["fullTime"]["away"],
        })
    return records


def main():
    data = fetch_matches()
    records = parse_matches(data)

    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/matches.csv", index=False)
    print(f"Extract completado: {len(df)} registros guardados en data/matches.csv")


if __name__ == "__main__":
    main()
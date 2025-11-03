import json
import sys
import requests

URL = "https://api.metatft.com/tft-leaderboard/v2/global?offset=0&limit=1000&queue=undefined"


def fetch_json(url: str, timeout: int = 30):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()


def save_json(data, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


try:
    data = fetch_json(URL)
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
    sys.exit(1)
except requests.exceptions.ConnectionError as e:
    print(f"Network error: {e}")
    sys.exit(1)
except requests.exceptions.Timeout as e:
    print(f"Timeout error: {e}")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"JSON parse error: {e}")
    sys.exit(1)

try:
    save_json(data, "data/leaderboard.json")
except OSError as e:
    print(f"File write error: {e}")
    sys.exit(1)

print(f"Saved JSON to leaderboard.json")

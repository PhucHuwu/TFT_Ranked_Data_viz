import json
import sys
import ssl
import urllib.request
import urllib.error

URL = "https://api.metatft.com/tft-leaderboard/v2/global?offset=0&limit=1000&queue=undefined"


def fetch_json(url: str, timeout: int = 1000):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        },
    )
    context = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=context) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        raw = resp.read().decode(charset, errors="replace")
        return json.loads(raw)


def save_json(data, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


try:
    data = fetch_json(URL)
except urllib.error.HTTPError as e:
    print(f"HTTP error {e.code}: {e.reason}")
    sys.exit(1)
except urllib.error.URLError as e:
    print(f"Network error: {e.reason}")
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

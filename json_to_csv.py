import csv
import json


def flatten(obj, parent_key="", sep="."):
    items = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten(v, new_key, sep))
    elif isinstance(obj, (list, tuple)):
        items[parent_key] = json.dumps(obj, ensure_ascii=False)
    else:
        items[parent_key] = obj
    return items


def convert_json_to_csv(input_file, output_file):
    with open(input_file, encoding="utf-8") as f:
        data = json.load(f)
    
    records = data["data"] if isinstance(data, dict) and "data" in data else data
    
    flattened = [flatten(rec) for rec in records]
    
    priority = ["rank",
                "rating_numeric",
                "num_played",
                "player_id", 
                "summoner_region",
                "riot_id",
                "puuid",
                "rating"]
    all_keys = set()
    for row in flattened:
        all_keys.update(row.keys())
    
    fieldnames = [f for f in priority if f in all_keys]
    fieldnames += sorted(k for k in all_keys if k not in priority)
    
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flattened)


convert_json_to_csv("leaderboard.json", "leaderboard.csv")
print("Saved CSV to leaderboard.csv")

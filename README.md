# TFT Ranked Data Visualization

A Python-based project for fetching and processing Teamfight Tactics (TFT) leaderboard data from the MetaTFT API.

## Overview

This project provides tools to:
- Fetch global TFT leaderboard data from the MetaTFT API
- Convert JSON data to CSV format for easier analysis
- Store and organize leaderboard data for visualization purposes

## Project Structure

```
TFT_Ranked_Data_viz/
├── tft_leaderboard_fetch.py    # Fetches leaderboard data from MetaTFT API
├── json_to_csv.py              # Converts JSON data to CSV format
├── data/                       # Data storage directory
│   ├── leaderboard.json        # Raw JSON data from API
│   └── leaderboard.csv         # Processed CSV data
└── README.md                   # Project documentation
```

## Features

- Fetches top 1000 players from the global TFT leaderboard
- Handles HTTP errors and network issues gracefully
- Flattens nested JSON structures for CSV conversion
- Prioritizes important fields (rank, rating, games played, etc.)
- UTF-8 encoding support for international player names

## Requirements

- Python 3.x
- Standard library modules (no external dependencies required)

## Usage

### Fetching Leaderboard Data

Run the leaderboard fetch script to download current leaderboard data:

```bash
python tft_leaderboard_fetch.py
```

This will:
- Fetch data from the MetaTFT API
- Save the raw JSON data to `data/leaderboard.json`

### Converting to CSV

After fetching the data, convert it to CSV format:

```bash
python json_to_csv.py
```

This will:
- Read the JSON file from `data/leaderboard.json`
- Flatten the nested structure
- Save the processed data to `data/leaderboard.csv`

## API Response Structure

The API returns data in the following structure:

### Meta Information
- `total`: Total number of players available
- `offset`: Starting position in the dataset
- `limit`: Maximum number of records returned

### Player Data

Each player record contains the following fields:

#### Basic Information
- `player_id`: Unique player identifier
- `summoner_region`: Server region (e.g., br1, na1, euw1)
- `riot_id`: Full Riot ID with tagline (e.g., "Player#TAG")
- `puuid`: Player Universally Unique Identifier
- `rating`: Formatted rating string (e.g., "CHALLENGER I 2071 LP")
- `rating_numeric`: Numerical rating value for sorting
- `num_played`: Total number of games played
- `rank`: Current leaderboard position

#### Statistics (stats object)

##### Overall Stats
- `num_played`: Total games played
- `place_sum`: Sum of all placement finishes
- `wins`: Total number of first-place finishes
- `appMatches`: Boolean indicating if app matches are available

##### Recent Results (RecentResult object)
- `num_played`: Games played in recent period (typically last 20 games)
- `wins`: First-place finishes in recent games
- `place_sum`: Sum of placements in recent games
- `lpChange`: LP (League Points) change in recent games
- `percentile_count`: Number of games included in percentile calculations
- `damage_percentile_sum`: Sum of damage percentile rankings
- `board_strength_percentile_sum`: Sum of board strength percentile rankings
- `avg_similarity`: Average team composition similarity score

###### Item Data (ItemData object)
- `Tank`: Number of tank items used
- `AD`: Number of Attack Damage items used
- `AP`: Number of Ability Power items used

###### Top Carries (topCarries array)
- `character_id`: Champion identifier (e.g., "TFT15_Braum")
- `count`: Number of times this champion was used as carry
- `avg`: Average placement when using this champion

##### Current Patch Results (currentPatchResult object)
Contains the same structure as RecentResult but filtered for the current game patch:
- `num_played`: Games in current patch
- `wins`: First places in current patch
- `place_sum`: Sum of placements
- `lpChange`: LP change for current patch
- `ItemData`: Item usage breakdown
- `topCarries`: Most used carry champions
- `damage_percentile_sum`: Damage percentile sum
- `board_strength_percentile_sum`: Board strength percentile sum
- `percentile_count`: Games in percentile calculation
- `avg_similarity`: Team composition similarity

## CSV Output Fields

The flattened CSV includes all nested fields with dot notation:

**Priority Fields (appear first):**
- `rank`
- `rating_numeric`
- `num_played`
- `player_id`
- `summoner_region`
- `riot_id`
- `puuid`
- `rating`

**Additional Fields (alphabetically sorted):**
- `stats.num_played`
- `stats.place_sum`
- `stats.wins`
- `stats.appMatches`
- `stats.RecentResult.num_played`
- `stats.RecentResult.wins`
- `stats.RecentResult.place_sum`
- `stats.RecentResult.lpChange`
- `stats.RecentResult.ItemData.Tank`
- `stats.RecentResult.ItemData.AD`
- `stats.RecentResult.ItemData.AP`
- `stats.RecentResult.topCarries` (as JSON string)
- `stats.RecentResult.damage_percentile_sum`
- `stats.RecentResult.board_strength_percentile_sum`
- `stats.RecentResult.percentile_count`
- `stats.RecentResult.avg_similarity`
- `stats.currentPatchResult.*` (similar structure to RecentResult)

## Error Handling

The scripts include error handling for:
- HTTP errors (invalid responses, server errors)
- Network errors (connection issues, timeouts)
- JSON parsing errors
- File I/O errors

## Data Source

Data is fetched from the MetaTFT API:
- Endpoint: `https://api.metatft.com/tft-leaderboard/v2/global`
- Limit: 1000 players
- Queue: All queues

## License

This project is open source and available for educational and personal use.

## Contributing

Contributions, issues, and feature requests are welcome.

## Author

PhucHuwu

# TFT Ranked Data Visualization

Analyze and visualize Teamfight Tactics (TFT) Challenger leaderboard data. This project fetches live leaderboard data, converts it to a flat CSV, performs multiple exploratory analyses, and produces interactive visualizations (Plotly, Folium) plus a word cloud image.

## Features

- Fetch global TFT leaderboard data from the MetaTFT API.
- Flatten nested JSON to CSV while preserving useful fields.
- Clean and analyze data across key themes:
  - ItemData distribution: AD, AP, Tank (Treemap)
  - Flexibility: avg_similarity (Histogram + Boxplot)
  - Top carries: frequency and co-picks (Word Cloud + Network Graph)
  - Playstyle: Eco vs High Tempo with regression (Scatter)
  - Region distribution and performance (Folium Map + Sunburst)
  - Performance correlations and distributions (Heatmap + Violin plots)
- One-click runner to generate all visualizations into `visualizations/`.

## Repository Structure

- `tft_leaderboard_fetch.py` — Download leaderboard JSON from MetaTFT.
- `json_to_csv.py` — Flatten JSON to `data/leaderboard.csv`.
- `cleandata.ipynb` — Optional cleaning step to produce `data/leaderboard_cleaned.csv` used by analyses.
- `run_all_analysis.py` — Orchestrate all analysis scripts and save outputs.
- `analysis_item_data.py` — Treemap of ItemData (AD/AP/Tank).
- `analysis_avg_similarity.py` — Flexibility (avg_similarity) distribution.
- `analysis_top_carries.py` — Word cloud and network graph for top carries.
- `analysis_playstyle.py` — Playstyle scatter (Eco vs High Tempo) with regression.
- `analysis_region.py` — Region Folium map and Plotly sunburst.
- `analysis_performance.py` — Correlation heatmap and violin plots.
- `data/` — Input and intermediate data (`leaderboard.json`, `leaderboard.csv`, `leaderboard_cleaned.csv`).
- `visualizations/` — Generated visual outputs (HTML/PNG).
- `index.html` — Optional landing page you can extend to link outputs.
- `requirements.txt` — Python dependencies.

## Prerequisites

- Python 3.9+ recommended
- Pip (or Pipenv/Poetry if you prefer)

## Setup

1) Clone the repository

```bash
git clone https://github.com/PhucHuwu/TFT_Ranked_Data_viz.git
cd TFT_Ranked_Data_viz
```

2) Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3) Install dependencies

```bash
pip install -r requirements.txt
```

## Data Pipeline

1) Fetch the leaderboard JSON

```bash
python tft_leaderboard_fetch.py
# writes: data/leaderboard.json
```

2) Convert JSON to CSV

```bash
python json_to_csv.py
# writes: data/leaderboard.csv
```

3) Clean and prepare the CSV used for analyses

- Open and run `cleandata.ipynb` to produce `data/leaderboard_cleaned.csv`.
- The analysis scripts expect this file and rely on columns created by flattening (e.g., `stats.RecentResult.ItemData.AD`).
- Quick test option: copy `data/leaderboard.csv` to `data/leaderboard_cleaned.csv` if you do not need extra cleaning (charts may be less accurate).

## Running Analyses

Generate everything at once:

```bash
python run_all_analysis.py
```

Run a specific analysis:

```bash
python analysis_item_data.py
python analysis_avg_similarity.py
python analysis_top_carries.py
python analysis_playstyle.py
python analysis_region.py
python analysis_performance.py
```

## Outputs

Files are written to `visualizations/`:

- `item_data_treemap.html` — Treemap of ItemData (AD/AP/Tank).
- `avg_similarity_distribution.html` — Flexibility histogram + boxplot.
- `top_carries_wordcloud.png` — Word cloud of most frequent carries.
- `top_carries_network.html` — Network graph of co-picked carries.
- `playstyle_scatter.html` — Scatter with regression for playstyle.
- `region_map.html` — Folium map of players by region.
- `region_sunburst.html` — Sunburst of regions by continent.
- `performance_heatmap.html` — Correlation heatmap of key metrics.
- `performance_violin.html` — Violin plots by region and performance tier.

Open the HTML files directly in your browser (double-click or serve locally). The PNG image opens with any image viewer.

## Notes and Tips

- API source: MetaTFT leaderboard endpoint is used in `tft_leaderboard_fetch.py`.
- Some console messages inside scripts may include Vietnamese text. If your terminal shows garbled characters on Windows, set UTF-8: `chcp 65001` in PowerShell before running.
- The scripts create `visualizations/` automatically if missing.
- Network errors or rate limits when fetching data: rerun after a short delay.

## Troubleshooting

- Missing `data/leaderboard_cleaned.csv`:
  - Ensure you ran `json_to_csv.py`, then the cleaning step/notebook to produce `leaderboard_cleaned.csv`.
  - For a quick run, duplicate `leaderboard.csv` as `leaderboard_cleaned.csv`.
- Plot files not created:
  - Check for exceptions printed in the terminal.
  - Verify the `visualizations/` directory is writeable and exists (it is auto-created by the runner).
- Unicode output looks incorrect:
  - Use a UTF-8 capable terminal, or set `PYTHONIOENCODING=utf-8`.
- Requests/SSL/network issues when fetching:
  - Confirm internet access and try again. The script retries are not built-in; rerun the command.

## Acknowledgments

- Data courtesy of MetaTFT API.
- Visualizations built with Plotly, Folium, Matplotlib/WordCloud, and NetworkX.

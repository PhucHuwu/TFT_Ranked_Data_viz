# 🎮 TFT Ranked Data Visualization & Analysis

## 📊 Project Overview

Comprehensive data analysis and visualization project for **TeamFight Tactics (TFT) Challenger players** across 15 global regions. This project analyzes gameplay patterns, champion preferences, playstyles, and performance metrics of 1000+ top-tier players.

---

## ✨ Features

### 6 Major Statistical Analyses:
1. **📦 Item Distribution (AD/AP/Tank)** - Player build preferences
2. **🔄 Flexibility Analysis** - Composition diversity vs one-tricking
3. **👑 Top Carries Analysis** - Most used champions
4. **⚔️ Playstyle Classification** - Eco vs High Tempo strategies
5. **🌍 Regional Distribution** - Player demographics across 15 regions
6. **📈 Performance Metrics** - Winrate & Average Placement correlation

### 9 Interactive & Static Visualizations:
- 🎨 **8 Interactive Charts** (Plotly/Folium)
- 🖼️ **1 Static Visualization** (WordCloud)

---

## 🚀 Quick Start

### 1. Installation
```bash
# Clone repository
git clone https://github.com/PhucHuwu/TFT_Ranked_Data_viz.git
cd TFT_Ranked_Data_viz

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Analysis
```bash
# Run all 6 analyses at once
python run_all_analysis.py

# Or run individually
python analysis_item_data.py
python analysis_avg_similarity.py
python analysis_top_carries.py
python analysis_playstyle.py
python analysis_region.py
python analysis_performance.py
```

### 3. View Results
- **Dashboard:** Open `index.html` in your browser
- **Individual Charts:** Open files in `visualizations/` folder
- **Summary Report:** Read `ANALYSIS_SUMMARY.md`

---

## 📁 Project Structure

```
TFT_Ranked_Data_viz/
│
├── 📄 index.html                         ⭐ Main Dashboard (START HERE!)
├── 📄 ANALYSIS_SUMMARY.md                📝 Detailed findings report
├── 📄 README_ANALYSIS.md                 📚 Technical documentation
├── 📄 QUICK_START.md                     🚀 Quick start guide
│
├── 📂 data/
│   ├── leaderboard.json                  🗂️ Raw data
│   ├── leaderboard.csv                   🗂️ Converted CSV
│   └── leaderboard_cleaned.csv           ✅ Cleaned dataset
│
├── 📂 visualizations/                    🎨 All output charts
│   ├── item_data_treemap.html           (Interactive - Plotly)
│   ├── avg_similarity_distribution.html  (Interactive - Plotly)
│   ├── top_carries_wordcloud.png         (Static - Matplotlib)
│   ├── top_carries_network.html          (Interactive - Plotly)
│   ├── playstyle_scatter.html            (Interactive - Plotly)
│   ├── region_map.html                   (Interactive - Folium)
│   ├── region_sunburst.html              (Interactive - Plotly)
│   ├── performance_heatmap.html          (Interactive - Plotly)
│   └── performance_violin.html           (Interactive - Plotly)
│
├── 🐍 Analysis Scripts:
│   ├── run_all_analysis.py               ▶️ Master script
│   ├── analysis_item_data.py             #1 Item distribution
│   ├── analysis_avg_similarity.py        #2 Flexibility analysis
│   ├── analysis_top_carries.py           #3 Champion usage
│   ├── analysis_playstyle.py             #4 Playstyle classification
│   ├── analysis_region.py                #5 Regional demographics
│   └── analysis_performance.py           #6 Performance metrics
│
├── 🛠️ Utilities:
│   ├── tft_leaderboard_fetch.py          📥 Data fetching
│   ├── json_to_csv.py                    🔄 Data conversion
│   └── cleandata.ipynb                   🧹 Data cleaning
│
└── 📄 requirements.txt                   📦 Python dependencies
```

---

## 📊 Key Findings

### 🏆 Top Insights:

1. **🛡️ Tank Meta Dominance**
   - Tank items: **41.66%** (highest)
   - AD items: 31.61%
   - AP items: 26.73%

2. **🎯 Flexible Gameplay**
   - **62.4%** players are flexible (diverse compositions)
   - Only **1.8%** spam one comp
   - Healthy meta diversity

3. **👑 Most Popular Carries**
   - **Lee Sin** - 164 picks (avg placement: 3.01)
   - **Braum** - 141 picks (avg placement: 3.09)
   - **K'Sante** - 100 picks (avg placement: 3.56)

4. **⚔️ High Tempo Wins More**
   - High Tempo: **17.97%** avg winrate (highest)
   - Eco: 16.08% avg winrate
   - Playstyle balance across 4 categories

5. **🌏 Asia Dominates**
   - **Vietnam: 34.6%** (346 players)
   - **Korea: 30.5%** (305 players)
   - Combined: **65.1%** of all Challenger players

6. **📈 Consistency is Key**
   - Winrate vs Avg Placement: **-0.73 correlation** (strong)
   - Elite tier (top 1.8%): ~30% WR, ~3.3 avg placement
   - Importance of top 4 consistency

---

## 📈 Visualizations

### Interactive Charts (8 total)
| # | Visualization | Type | Technology | Description |
|---|---------------|------|------------|-------------|
| 1 | **Treemap** | Hierarchical | Plotly | Item distribution (AD/AP/Tank) |
| 2 | **Histogram + Boxplot** | Distribution | Plotly | Flexibility analysis |
| 3 | **Network Graph** | Relationship | Plotly | Champion connections |
| 4 | **Scatter + Regression** | Correlation | Plotly | Playstyle classification |
| 5 | **World Map** | Geographic | Folium | Regional player distribution |
| 6 | **Sunburst** | Hierarchical | Plotly | Continent → Region breakdown |
| 7 | **Heatmap** | Correlation | Plotly | Performance metrics correlation |
| 8 | **Violin Plot** | Distribution | Plotly | Performance by region/tier |

### Static Charts (1 total)
| # | Visualization | Type | Technology | Description |
|---|---------------|------|------------|-------------|
| 9 | **WordCloud** | Text | Matplotlib | Champion frequency |

**Total: 9 visualizations** (8 interactive + 1 static)

---

## 🔬 Technical Details

### Data Source
- **Source:** TFT Official API / Leaderboard
- **Sample Size:** 1000 Challenger players
- **Regions:** 15 (VN, BR, EUNE, EUW, JP, KR, LAN, LAS, ME, NA, OCE, PBE, RU, SEA, TR, TW)
- **Metrics Analyzed:**
  - ItemData (AD, AP, Tank counts)
  - avg_similarity (composition diversity)
  - topCarries (JSON data)
  - damage_percentile_sum, board_strength_percentile_sum
  - Winrate, Average Placement, Rating

### Technologies Used
| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **Interactive Viz** | Plotly, Folium |
| **Static Viz** | Matplotlib, Seaborn, WordCloud |
| **Network Analysis** | NetworkX |
| **Statistics** | SciPy |
| **Web** | HTML, CSS, JavaScript |

### Requirements
See `requirements.txt`:
```
pandas
numpy
matplotlib
seaborn
plotly
altair
wordcloud
folium
networkx
scipy
```

---

## 📚 Documentation

| File | Description |
|------|-------------|
| `README.md` | This file - Project overview |
| `README_ANALYSIS.md` | Detailed methodology & analysis explanation |
| `ANALYSIS_SUMMARY.md` | Comprehensive findings report with all insights |
| `QUICK_START.md` | Quick start guide for viewing results |

---

## 🎯 Use Cases

### For Players:
- 📊 Understand current meta trends
- 🎯 Learn which carries to prioritize
- 💡 Discover optimal playstyles
- 📈 Benchmark your performance

### For Analysts:
- 🔍 Deep dive into regional differences
- 📉 Correlation analysis between metrics
- 🎨 Data visualization best practices
- 🐍 Reusable Python analysis scripts

### For Educators:
- 📚 Example of comprehensive data analysis
- 🎨 Showcase of diverse visualization types
- 💻 Clean, documented Python code
- 📊 Real-world dataset analysis

---

## 🌟 Highlights

✅ **6 comprehensive analyses**  
✅ **9 professional visualizations**  
✅ **8 interactive charts** (Plotly/Folium)  
✅ **1000+ players analyzed**  
✅ **15 regions covered**  
✅ **Beautiful HTML dashboard**  
✅ **Detailed documentation**  
✅ **Reusable Python scripts**  
✅ **Clean, modular code**  
✅ **Open source**  

---

## 📖 How to Read This Project

### For Quick Overview:
1. Open `index.html` - Beautiful dashboard
2. Read `QUICK_START.md` - 5-minute guide
3. Check key findings in this README

### For Deep Analysis:
1. Read `ANALYSIS_SUMMARY.md` - Full report
2. Read `README_ANALYSIS.md` - Methodology
3. Explore individual visualizations
4. Review Python scripts for implementation

### For Developers:
1. Check `requirements.txt` - Dependencies
2. Review analysis scripts (`.py` files)
3. Understand data pipeline:
   - Fetch → Convert → Clean → Analyze → Visualize
4. Modify and extend as needed

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- 🔄 Add more statistical analyses
- 🎨 Create additional visualizations
- 📊 Analyze different patches/seasons
- 🌍 Add more regional breakdowns
- 🤖 Machine learning predictions
- 📱 Mobile-friendly dashboard

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**PhucHuwu**
- GitHub: [@PhucHuwu](https://github.com/PhucHuwu)
- Project: [TFT_Ranked_Data_viz](https://github.com/PhucHuwu/TFT_Ranked_Data_viz)

---

## 🙏 Acknowledgments

- TFT API for providing leaderboard data
- Plotly team for amazing interactive visualization library
- Python data science community
- All Challenger players whose data made this analysis possible

---

## 📞 Support

For questions, issues, or feedback:
- 📧 Open an issue on GitHub
- 📝 Check documentation files
- 💬 Review code comments

---

## 🎉 Quick Links

- 🏠 [Main Dashboard](index.html) - Start here!
- 📊 [Analysis Summary](ANALYSIS_SUMMARY.md) - Key findings
- 🚀 [Quick Start Guide](QUICK_START.md) - Get started
- 📚 [Technical Docs](README_ANALYSIS.md) - Methodology

---

**⭐ If you find this project useful, please give it a star!**

---

*Last Updated: November 2025*

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

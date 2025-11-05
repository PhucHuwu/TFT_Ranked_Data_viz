# TFT Ranked Data Visualization

A comprehensive data analysis and visualization tool for Teamfight Tactics (TFT) Challenger leaderboard data. This project provides automated data collection, processing, and analysis capabilities to generate insights into player statistics, itemization patterns, playstyles, and regional distributions through interactive visualizations.

## Overview

This project delivers an end-to-end pipeline for analyzing TFT Challenger leaderboard data, from data acquisition through MetaTFT API to generating sophisticated visual analytics. The system processes nested JSON data structures, performs multi-dimensional statistical analyses, and produces publication-ready visualizations using industry-standard libraries including Plotly, Folium, and NetworkX.

## Key Features

**Data Collection and Processing**
- Automated retrieval of global TFT Challenger leaderboard data via MetaTFT API
- Intelligent JSON-to-CSV conversion maintaining data integrity and nested field relationships
- Robust data cleaning and preprocessing pipeline

**Analytical Capabilities**
- Item composition analysis examining AD, AP, and Tank distributions through treemap visualizations
- Flexibility metrics assessment using average similarity scores with statistical distributions
- Carry champion frequency analysis and co-occurrence patterns via word clouds and network graphs
- Playstyle characterization comparing Economy-focused versus High Tempo strategies with regression modeling
- Geographic distribution analysis and performance metrics across regions using choropleth maps and hierarchical visualizations
- Comprehensive performance correlation analysis through heatmaps and distributional comparisons

**Automation**
- Unified execution script for batch generation of all analytical outputs
- Modular architecture supporting individual analysis execution


## Project Structure

```
TFT_Ranked_Data_viz/
├── tft_leaderboard_fetch.py      # Data acquisition from MetaTFT API
├── json_to_csv.py                # JSON to CSV conversion utility
├── cleandata.ipynb               # Data cleaning and preprocessing notebook
├── run_all_analysis.py           # Orchestration script for all analyses
├── analysis_item_data.py         # Item composition treemap generator
├── analysis_avg_similarity.py    # Flexibility metrics analysis
├── analysis_top_carries.py       # Carry champion analysis and network visualization
├── analysis_playstyle.py         # Playstyle scatter plot with regression
├── analysis_region.py            # Geographic distribution analysis
├── analysis_performance.py       # Performance correlation and distribution analysis
├── data/                         # Data directory
│   ├── leaderboard.json          # Raw API response
│   ├── leaderboard.csv           # Flattened dataset
│   └── leaderboard_cleaned.csv   # Processed dataset for analysis
├── visualizations/               # Generated visualization outputs
│   ├── item_data_treemap.html
│   ├── avg_similarity_distribution.html
│   ├── top_carries_wordcloud.png
│   ├── top_carries_network.html
│   ├── playstyle_scatter.html
│   ├── region_map.html
│   ├── region_sunburst.html
│   ├── performance_heatmap.html
│   └── performance_violin.html
├── index.html                    # Landing page template
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```


## System Requirements

- Python 3.9 or higher
- pip package manager
- Virtual environment support (recommended)
- Internet connection for data acquisition

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PhucHuwu/TFT_Ranked_Data_viz.git
cd TFT_Ranked_Data_viz
```

### 2. Create Virtual Environment

**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


## Usage

### Complete Analysis Pipeline

The following workflow demonstrates the full data acquisition and analysis process:

#### Step 1: Data Acquisition

Retrieve the latest TFT Challenger leaderboard data from MetaTFT API:

```bash
python tft_leaderboard_fetch.py
```

This generates `data/leaderboard.json` containing raw API response data.

#### Step 2: Data Transformation

Convert nested JSON structure to tabular CSV format:

```bash
python json_to_csv.py
```

This produces `data/leaderboard.csv` with flattened data fields.

#### Step 3: Data Preprocessing

Execute the Jupyter notebook for data cleaning and preparation:

1. Open `cleandata.ipynb` in Jupyter Notebook or JupyterLab
2. Run all cells sequentially
3. Output: `data/leaderboard_cleaned.csv`

**Note:** Analysis scripts require `leaderboard_cleaned.csv`. For quick testing without custom cleaning, you may duplicate `leaderboard.csv` as `leaderboard_cleaned.csv`, though this may reduce analytical accuracy.

#### Step 4: Generate Visualizations

**Option A: Batch Processing (Recommended)**

Execute all analyses simultaneously:

```bash
python run_all_analysis.py
```

**Option B: Individual Analysis Execution**

Run specific analysis modules:

```bash
python analysis_item_data.py          # Item composition treemap
python analysis_avg_similarity.py     # Flexibility metrics
python analysis_top_carries.py        # Carry champion analysis
python analysis_playstyle.py          # Playstyle characterization
python analysis_region.py             # Geographic distribution
python analysis_performance.py        # Performance correlations
```


## Output Visualizations

All visualization files are saved to the `visualizations/` directory:

| File | Type | Description |
|------|------|-------------|
| `item_data_treemap.html` | Interactive HTML | Hierarchical treemap displaying ItemData distribution across AD, AP, and Tank categories |
| `avg_similarity_distribution.html` | Interactive HTML | Statistical distribution of flexibility metrics via histogram and boxplot |
| `top_carries_wordcloud.png` | Static Image | Word cloud visualization of carry champion frequency |
| `top_carries_network.html` | Interactive HTML | Network graph illustrating co-occurrence patterns among carry champions |
| `playstyle_scatter.html` | Interactive HTML | Scatter plot with regression analysis comparing Economy vs High Tempo playstyles |
| `region_map.html` | Interactive HTML | Geographic choropleth map showing player distribution by region |
| `region_sunburst.html` | Interactive HTML | Hierarchical sunburst chart of regional distributions by continent |
| `performance_heatmap.html` | Interactive HTML | Correlation heatmap analyzing relationships between performance metrics |
| `performance_violin.html` | Interactive HTML | Violin plots comparing performance distributions across regions and tiers |

### Viewing Visualizations

- **HTML files:** Open directly in any modern web browser (Chrome, Firefox, Edge, Safari)
- **PNG files:** View with any standard image viewer application
- **Alternative:** Serve files locally using Python's built-in HTTP server:
  ```bash
  python -m http.server 8000
  # Navigate to http://localhost:8000/visualizations/
  ```


## Technical Notes

### Data Source
This project utilizes the MetaTFT API leaderboard endpoint for data acquisition. The API provides comprehensive statistics for TFT Challenger players globally.

### Character Encoding
Some console output messages may contain Vietnamese text. If experiencing character encoding issues on Windows:

```powershell
chcp 65001  # Set console to UTF-8 encoding
```

Alternatively, set the Python I/O encoding environment variable:

```powershell
$env:PYTHONIOENCODING="utf-8"
```

### Directory Management
The `visualizations/` directory is created automatically by the orchestration script if it does not exist. Ensure write permissions are granted for the project directory.

### API Considerations
- Network connectivity is required for data fetching operations
- API rate limits may apply; if encountering errors, wait briefly before retrying
- No built-in retry mechanism is implemented; manual re-execution is required for failed requests


## Troubleshooting

### Missing leaderboard_cleaned.csv

**Symptom:** Analysis scripts fail with file not found error.

**Solution:**
1. Verify execution of `json_to_csv.py` to generate `leaderboard.csv`
2. Execute all cells in `cleandata.ipynb` to produce `leaderboard_cleaned.csv`
3. Quick workaround: Duplicate `leaderboard.csv` as `leaderboard_cleaned.csv`
   ```bash
   Copy-Item data\leaderboard.csv data\leaderboard_cleaned.csv
   ```
   Note: This bypass may reduce analytical accuracy.

### Visualization Files Not Generated

**Symptom:** Expected output files missing from `visualizations/` directory.

**Solution:**
1. Check terminal output for Python exceptions or error messages
2. Verify `visualizations/` directory exists and has write permissions
3. Ensure all dependencies are installed correctly:
   ```bash
   pip install -r requirements.txt --upgrade
   ```
4. Run individual analysis scripts to isolate the failing module

### Unicode/Encoding Display Issues

**Symptom:** Garbled text or encoding errors in terminal output.

**Solution:**
- Set terminal encoding to UTF-8 (Windows PowerShell):
  ```powershell
  chcp 65001
  ```
- Set Python I/O encoding environment variable:
  ```powershell
  $env:PYTHONIOENCODING="utf-8"
  ```
- Use a UTF-8 compatible terminal (Windows Terminal, VS Code integrated terminal)

### Network/API Request Failures

**Symptom:** Data fetching fails with connection errors or timeouts.

**Solution:**
1. Verify internet connectivity
2. Check if MetaTFT API is accessible
3. Wait 60 seconds and retry the request
4. Consider implementing custom retry logic if issues persist:
   ```python
   # Add to tft_leaderboard_fetch.py if needed
   import time
   from requests.adapters import HTTPAdapter
   from requests.packages.urllib3.util.retry import Retry
   ```

### Dependency Conflicts

**Symptom:** Import errors or version compatibility warnings.

**Solution:**
1. Create a fresh virtual environment
2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```
3. Verify Python version compatibility (3.9+):
   ```bash
   python --version
   ```


## Technologies

**Programming Language**
- Python 3.9+

**Data Processing**
- pandas - Data manipulation and analysis
- NumPy - Numerical computing

**Visualization Libraries**
- Plotly - Interactive web-based visualizations
- Folium - Geographic mapping
- Matplotlib - Static plotting
- WordCloud - Text visualization
- NetworkX - Network graph analysis

**Data Acquisition**
- requests - HTTP library for API calls

**Development Tools**
- Jupyter Notebook - Interactive data analysis environment

## Contributing

Contributions are welcome. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes with descriptive messages
4. Push to your fork (`git push origin feature/enhancement`)
5. Submit a Pull Request with detailed description

## License

This project is available for educational and research purposes. Please refer to the repository license file for specific terms.

## Acknowledgments

- **Data Provider:** MetaTFT API for Challenger leaderboard data
- **Visualization Libraries:** Plotly, Folium, Matplotlib, WordCloud, NetworkX development teams
- **Community:** TFT data analysis community for insights and methodology references

## Contact

For questions, issues, or suggestions:
- Create an issue in the GitHub repository
- Contact: PhucHuwu (GitHub)

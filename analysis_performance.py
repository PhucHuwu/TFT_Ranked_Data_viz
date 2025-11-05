import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

df = pd.read_csv('data/leaderboard_cleaned.csv')

df['winrate'] = (df['stats.wins'] / df['stats.num_played'] * 100)
df['avg_placement'] = df['stats.place_sum'] / df['stats.num_played']
df['top4_rate'] = (df['stats.wins'] / df['stats.num_played'] * 100)

perf_data = df[['winrate', 'avg_placement', 'summoner_region', 'rating_numeric', 
                'stats.num_played', 'stats.RecentResult.avg_similarity']].dropna()

def classify_performance(row):
    wr = row['winrate']
    ap = row['avg_placement']
    
    if wr >= 25 and ap <= 3.5:
        return 'Elite'
    elif wr >= 20 and ap <= 4.0:
        return 'High Performer'
    elif wr >= 15 and ap <= 4.5:
        return 'Above Average'
    else:
        return 'Average'

perf_data['performance_tier'] = perf_data.apply(classify_performance, axis=1)

corr_cols = ['winrate', 'avg_placement', 'rating_numeric', 'stats.num_played', 
             'stats.RecentResult.avg_similarity']
corr_data = perf_data[corr_cols].copy()
corr_data.columns = ['Winrate', 'Avg Placement', 'Rating', 'Games Played', 'Avg Similarity']

corr_matrix = corr_data.corr()

fig_heatmap = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    colorscale='RdBu',
    zmid=0,
    text=corr_matrix.values.round(3),
    texttemplate='%{text}',
    textfont={"size": 12},
    colorbar=dict(title="Correlation")
))

fig_heatmap.update_layout(
    title='Heatmap Tương quan - Các chỉ số Performance<br><sub>Giá trị từ -1 (tương quan nghịch) đến +1 (tương quan thuận)</sub>',
    height=600,
    width=800,
    xaxis=dict(side='bottom'),
    font=dict(size=11)
)

fig_heatmap.write_html('visualizations/performance_heatmap.html')
print("✓ Đã tạo biểu đồ: visualizations/performance_heatmap.html")

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Winrate Distribution by Region',
        'Avg Placement Distribution by Region',
        'Winrate by Performance Tier',
        'Avg Placement by Performance Tier'
    ),
    specs=[[{"type": "violin"}, {"type": "violin"}],
           [{"type": "violin"}, {"type": "violin"}]]
)

top_regions = perf_data['summoner_region'].value_counts().head(8).index.tolist()
region_data = perf_data[perf_data['summoner_region'].isin(top_regions)]

for region in top_regions:
    region_subset = region_data[region_data['summoner_region'] == region]
    fig.add_trace(
        go.Violin(
            y=region_subset['winrate'],
            name=region.upper(),
            box_visible=True,
            meanline_visible=True,
            showlegend=False
        ),
        row=1, col=1
    )

for region in top_regions:
    region_subset = region_data[region_data['summoner_region'] == region]
    fig.add_trace(
        go.Violin(
            y=region_subset['avg_placement'],
            name=region.upper(),
            box_visible=True,
            meanline_visible=True,
            showlegend=False
        ),
        row=1, col=2
    )

for tier in ['Elite', 'High Performer', 'Above Average', 'Average']:
    tier_data = perf_data[perf_data['performance_tier'] == tier]
    if len(tier_data) > 0:
        fig.add_trace(
            go.Violin(
                y=tier_data['winrate'],
                name=tier,
                box_visible=True,
                meanline_visible=True,
                showlegend=False
            ),
            row=2, col=1
        )

for tier in ['Elite', 'High Performer', 'Above Average', 'Average']:
    tier_data = perf_data[perf_data['performance_tier'] == tier]
    if len(tier_data) > 0:
        fig.add_trace(
            go.Violin(
                y=tier_data['avg_placement'],
                name=tier,
                box_visible=True,
                meanline_visible=True,
                showlegend=False
            ),
            row=2, col=2
        )

fig.update_yaxes(title_text="Winrate (%)", row=1, col=1)
fig.update_yaxes(title_text="Avg Placement", row=1, col=2)
fig.update_yaxes(title_text="Winrate (%)", row=2, col=1)
fig.update_yaxes(title_text="Avg Placement", row=2, col=2)

fig.update_layout(
    title_text='Violin Plot - Phân tích Performance theo Region và Tier<br><sub>Interactive visualization</sub>',
    height=900,
    showlegend=False,
    font=dict(size=10)
)

fig.write_html('visualizations/performance_violin.html')
print("✓ Đã tạo biểu đồ: visualizations/performance_violin.html")

print("\n=== THỐNG KÊ HIỆU SUẤT NGƯỜI CHƠI ===")
print(f"Winrate:")
print(f"  Mean: {perf_data['winrate'].mean():.2f}%")
print(f"  Median: {perf_data['winrate'].median():.2f}%")
print(f"  Std: {perf_data['winrate'].std():.2f}%")
print(f"  Min: {perf_data['winrate'].min():.2f}%")
print(f"  Max: {perf_data['winrate'].max():.2f}%")

print(f"\nAverage Placement:")
print(f"  Mean: {perf_data['avg_placement'].mean():.2f}")
print(f"  Median: {perf_data['avg_placement'].median():.2f}")
print(f"  Std: {perf_data['avg_placement'].std():.2f}")
print(f"  Min: {perf_data['avg_placement'].min():.2f}")
print(f"  Max: {perf_data['avg_placement'].max():.2f}")

print("\n=== PHÂN LOẠI PERFORMANCE ===")
tier_counts = perf_data['performance_tier'].value_counts()
for tier, count in tier_counts.items():
    pct = count / len(perf_data) * 100
    avg_wr = perf_data[perf_data['performance_tier'] == tier]['winrate'].mean()
    avg_place = perf_data[perf_data['performance_tier'] == tier]['avg_placement'].mean()
    print(f"{tier}: {count} ({pct:.1f}%) - Avg WR: {avg_wr:.2f}% - Avg Place: {avg_place:.2f}")

print("\n=== TƯƠNG QUAN ===")
print(f"Winrate vs Avg Placement: {perf_data['winrate'].corr(perf_data['avg_placement']):.4f}")
print(f"Winrate vs Rating: {perf_data['winrate'].corr(perf_data['rating_numeric']):.4f}")
print(f"Avg Placement vs Rating: {perf_data['avg_placement'].corr(perf_data['rating_numeric']):.4f}")

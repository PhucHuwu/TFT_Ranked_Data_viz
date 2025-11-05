import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import numpy as np

df = pd.read_csv('data/leaderboard_cleaned.csv')

damage_data = df[['stats.RecentResult.damage_percentile_sum', 
                   'stats.RecentResult.board_strength_percentile_sum',
                   'summoner_region',
                   'stats.wins',
                   'stats.num_played']].dropna()

damage_data = damage_data.rename(columns={
    'stats.RecentResult.damage_percentile_sum': 'damage',
    'stats.RecentResult.board_strength_percentile_sum': 'board_strength',
    'summoner_region': 'region'
})

damage_data['winrate'] = (damage_data['stats.wins'] / damage_data['stats.num_played'] * 100)

def classify_playstyle(row):
    damage = row['damage']
    board = row['board_strength']
    
    damage_median = damage_data['damage'].median()
    board_median = damage_data['board_strength'].median()
    
    if damage > damage_median and board > board_median:
        return 'High Tempo (Aggressive)'
    elif damage < damage_median and board < board_median:
        return 'Eco (Conservative)'
    elif damage > damage_median:
        return 'Damage Focus'
    else:
        return 'Board Strength Focus'

damage_data['playstyle'] = damage_data.apply(classify_playstyle, axis=1)

slope, intercept, r_value, p_value, std_err = stats.linregress(
    damage_data['damage'], 
    damage_data['board_strength']
)

x_range = np.linspace(damage_data['damage'].min(), damage_data['damage'].max(), 100)
y_pred = slope * x_range + intercept

fig = px.scatter(
    damage_data,
    x='damage',
    y='board_strength',
    color='playstyle',
    size='winrate',
    hover_data=['region', 'winrate'],
    title='Phân tích Phong cách chơi: Eco vs High Tempo<br><sub>Scatter Plot với Regression Line</sub>',
    labels={
        'damage': 'Damage Percentile Sum (Sức mạnh đội hình)',
        'board_strength': 'Board Strength Percentile Sum (Giá trị đội hình)',
        'playstyle': 'Phong cách chơi',
        'winrate': 'Winrate (%)'
    },
    color_discrete_map={
        'High Tempo (Aggressive)': '#FF6B6B',
        'Eco (Conservative)': '#4ECDC4',
        'Damage Focus': '#FFE66D',
        'Board Strength Focus': '#95E1D3'
    }
)

fig.add_trace(
    go.Scatter(
        x=x_range,
        y=y_pred,
        mode='lines',
        name=f'Regression Line (R² = {r_value**2:.3f})',
        line=dict(color='red', width=3, dash='dash'),
        hovertemplate='Predicted: %{y:.1f}<extra></extra>'
    )
)

fig.add_hline(
    y=damage_data['board_strength'].median(),
    line_dash="dot",
    line_color="gray",
    annotation_text="Median Board Strength"
)

fig.add_vline(
    x=damage_data['damage'].median(),
    line_dash="dot",
    line_color="gray",
    annotation_text="Median Damage"
)

fig.update_layout(
    height=700,
    font=dict(size=11),
    hovermode='closest'
)

fig.write_html('visualizations/playstyle_scatter.html')
print("✓ Đã tạo biểu đồ: visualizations/playstyle_scatter.html")

print("\n=== THỐNG KÊ PHONG CÁCH CHƠI ===")
print(f"\nHệ số tương quan (R²): {r_value**2:.4f}")
print(f"P-value: {p_value:.6f}")
print(f"Slope: {slope:.4f}")

print("\n=== PHÂN BỐ PHONG CÁCH CHƠI ===")
playstyle_counts = damage_data['playstyle'].value_counts()
for style, count in playstyle_counts.items():
    pct = count / len(damage_data) * 100
    avg_wr = damage_data[damage_data['playstyle'] == style]['winrate'].mean()
    print(f"{style}: {count} người ({pct:.1f}%) - Avg WR: {avg_wr:.2f}%")

print("\n=== THỐNG KÊ THEO CHỈ SỐ ===")
print(f"Damage Percentile Sum:")
print(f"  Mean: {damage_data['damage'].mean():.2f}")
print(f"  Median: {damage_data['damage'].median():.2f}")
print(f"  Std: {damage_data['damage'].std():.2f}")

print(f"\nBoard Strength Percentile Sum:")
print(f"  Mean: {damage_data['board_strength'].mean():.2f}")
print(f"  Median: {damage_data['board_strength'].median():.2f}")
print(f"  Std: {damage_data['board_strength'].std():.2f}")

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

df = pd.read_csv('data/leaderboard_cleaned.csv')

similarity = df['stats.RecentResult.avg_similarity'].dropna()

fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=(
        'Phân bố độ tương đồng đội hình (Histogram)',
        'Boxplot - Phân tích outliers'
    ),
    row_heights=[0.7, 0.3],
    vertical_spacing=0.12
)

fig.add_trace(
    go.Histogram(
        x=similarity,
        nbinsx=50,
        name='Frequency',
        marker=dict(
            color=similarity,
            colorscale='Viridis',
            line=dict(color='white', width=1)
        ),
        hovertemplate='Similarity: %{x:.3f}<br>Count: %{y}<extra></extra>'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Box(
        x=similarity,
        name='Distribution',
        marker=dict(color='rgb(107, 174, 214)'),
        boxmean='sd',
        hovertemplate='Value: %{x:.3f}<extra></extra>'
    ),
    row=2, col=1
)

mean_val = similarity.mean()
median_val = similarity.median()

fig.add_vline(x=mean_val, line_dash="dash", line_color="red", 
              annotation_text=f"Mean: {mean_val:.3f}", row=1, col=1)
fig.add_vline(x=median_val, line_dash="dash", line_color="green", 
              annotation_text=f"Median: {median_val:.3f}", row=1, col=1)

fig.update_xaxes(title_text="Độ tương đồng trung bình", row=1, col=1)
fig.update_xaxes(title_text="Độ tương đồng trung bình", row=2, col=1)
fig.update_yaxes(title_text="Số lượng người chơi", row=1, col=1)

fig.update_layout(
    title_text='Phân tích độ Flexible của người chơi<br><sub>Giá trị thấp = Flexible (đa dạng đội hình), Giá trị cao = Spam comp</sub>',
    showlegend=False,
    height=800,
    font=dict(size=11)
)

fig.write_html('visualizations/avg_similarity_distribution.html')
print("✓ Đã tạo biểu đồ: visualizations/avg_similarity_distribution.html")

print("\n=== THỐNG KÊ ĐỘ FLEXIBLE ===")
print(f"Mean (Trung bình): {mean_val:.4f}")
print(f"Median (Trung vị): {median_val:.4f}")
print(f"Std (Độ lệch chuẩn): {similarity.std():.4f}")
print(f"Min: {similarity.min():.4f}")
print(f"Max: {similarity.max():.4f}")
print(f"Q1 (25%): {similarity.quantile(0.25):.4f}")
print(f"Q3 (75%): {similarity.quantile(0.75):.4f}")

flexible_count = (similarity < 0.25).sum()
moderate_count = ((similarity >= 0.25) & (similarity < 0.50)).sum()
spam_count = (similarity >= 0.50).sum()

print(f"\n=== PHÂN LOẠI NGƯỜI CHƠI ===")
print(f"Flexible (< 0.25): {flexible_count} người ({flexible_count/len(similarity)*100:.1f}%)")
print(f"Moderate (0.25-0.50): {moderate_count} người ({moderate_count/len(similarity)*100:.1f}%)")
print(f"Spam comp (>= 0.50): {spam_count} người ({spam_count/len(similarity)*100:.1f}%)")

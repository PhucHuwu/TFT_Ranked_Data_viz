import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Đọc dữ liệu
df = pd.read_csv('data/leaderboard_cleaned.csv')

# Tính tổng số trang bị theo loại
total_ad = df['stats.RecentResult.ItemData.AD'].sum()
total_ap = df['stats.RecentResult.ItemData.AP'].sum()
total_tank = df['stats.RecentResult.ItemData.Tank'].sum()

# Tạo DataFrame cho visualization
item_data = pd.DataFrame({
    'Category': ['AD (Vật lý)', 'AP (Phép thuật)', 'Tank (Đỡ đòn)'],
    'Count': [total_ad, total_ap, total_tank],
    'Percentage': [
        total_ad / (total_ad + total_ap + total_tank) * 100,
        total_ap / (total_ad + total_ap + total_tank) * 100,
        total_tank / (total_ad + total_ap + total_tank) * 100
    ]
})

# Tạo Treemap với Plotly (Interactive)
fig = px.treemap(
    item_data,
    path=['Category'],
    values='Count',
    title='Phân bố trang bị theo loại (AD, AP, Tank)<br><sub>Phong cách chơi của người chơi Challenger</sub>',
    color='Percentage',
    color_continuous_scale='RdYlGn',
    hover_data={'Count': ':,', 'Percentage': ':.2f'}
)

fig.update_traces(
    textinfo='label+value+percent parent',
    textfont_size=14,
    marker=dict(line=dict(width=2, color='white'))
)

fig.update_layout(
    font=dict(size=12),
    height=600,
    coloraxis_colorbar=dict(
        title="Phần trăm (%)",
        ticksuffix="%"
    )
)

# Lưu biểu đồ
fig.write_html('visualizations/item_data_treemap.html')
print("✓ Đã tạo biểu đồ: visualizations/item_data_treemap.html")

# In thống kê
print("\n=== THỐNG KÊ TRANG BỊ THEO LOẠI ===")
print(f"Tổng AD (Vật lý): {total_ad:,} ({item_data.loc[0, 'Percentage']:.2f}%)")
print(f"Tổng AP (Phép): {total_ap:,} ({item_data.loc[1, 'Percentage']:.2f}%)")
print(f"Tổng Tank (Đỡ đòn): {total_tank:,} ({item_data.loc[2, 'Percentage']:.2f}%)")
print(f"\nPhong cách chơi phổ biến nhất: {item_data.loc[item_data['Count'].idxmax(), 'Category']}")

# Thống kê chi tiết hơn: phân bố theo region
print("\n=== PHÂN BỐ THEO KHU VỰC ===")
region_item = df.groupby('summoner_region')[['stats.RecentResult.ItemData.AD', 
                                              'stats.RecentResult.ItemData.AP', 
                                              'stats.RecentResult.ItemData.Tank']].mean()
print(region_item.round(2))

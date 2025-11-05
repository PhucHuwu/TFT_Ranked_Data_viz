import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv('data/leaderboard_cleaned.csv')

region_info = {
    'vn2': {'name': 'Vietnam', 'lat': 16.0, 'lon': 108.0, 'continent': 'Asia'},
    'br1': {'name': 'Brazil', 'lat': -14.0, 'lon': -51.0, 'continent': 'Americas'},
    'eun1': {'name': 'EU Nordic & East', 'lat': 59.0, 'lon': 18.0, 'continent': 'Europe'},
    'euw1': {'name': 'EU West', 'lat': 50.0, 'lon': 10.0, 'continent': 'Europe'},
    'jp1': {'name': 'Japan', 'lat': 36.0, 'lon': 138.0, 'continent': 'Asia'},
    'kr': {'name': 'Korea', 'lat': 37.5, 'lon': 127.0, 'continent': 'Asia'},
    'la1': {'name': 'LAN', 'lat': 23.0, 'lon': -102.0, 'continent': 'Americas'},
    'la2': {'name': 'LAS', 'lat': -34.0, 'lon': -64.0, 'continent': 'Americas'},
    'me1': {'name': 'Middle East', 'lat': 24.0, 'lon': 54.0, 'continent': 'Middle East'},
    'na1': {'name': 'North America', 'lat': 37.0, 'lon': -95.0, 'continent': 'Americas'},
    'oc1': {'name': 'Oceania', 'lat': -25.0, 'lon': 133.0, 'continent': 'Oceania'},
    'pbe1': {'name': 'PBE', 'lat': 37.0, 'lon': -122.0, 'continent': 'Test Server'},
    'ru': {'name': 'Russia', 'lat': 60.0, 'lon': 100.0, 'continent': 'Europe'},
    'sg2': {'name': 'SEA', 'lat': 1.3, 'lon': 103.8, 'continent': 'Asia'},
    'tr1': {'name': 'Turkey', 'lat': 39.0, 'lon': 35.0, 'continent': 'Europe'},
    'tw2': {'name': 'Taiwan', 'lat': 23.7, 'lon': 121.0, 'continent': 'Asia'}
}

region_counts = df['summoner_region'].value_counts().reset_index()
region_counts.columns = ['region_code', 'player_count']

region_counts['region_name'] = region_counts['region_code'].map(lambda x: region_info.get(x, {}).get('name', x))
region_counts['lat'] = region_counts['region_code'].map(lambda x: region_info.get(x, {}).get('lat', 0))
region_counts['lon'] = region_counts['region_code'].map(lambda x: region_info.get(x, {}).get('lon', 0))
region_counts['continent'] = region_counts['region_code'].map(lambda x: region_info.get(x, {}).get('continent', 'Unknown'))

region_stats = df.groupby('summoner_region').agg({
    'stats.wins': 'sum',
    'stats.num_played': 'sum',
    'rating_numeric': 'mean'
}).reset_index()

region_stats['avg_winrate'] = (region_stats['stats.wins'] / region_stats['stats.num_played'] * 100)
region_counts = region_counts.merge(region_stats[['summoner_region', 'avg_winrate', 'rating_numeric']], 
                                     left_on='region_code', right_on='summoner_region', how='left')

m = folium.Map(location=[20, 0], zoom_start=2, tiles='OpenStreetMap')

for idx, row in region_counts.iterrows():
    if row['lat'] != 0 and row['lon'] != 0:
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=row['player_count'] / 10,
            popup=f"""
                <b>{row['region_name']}</b><br>
                Players: {row['player_count']}<br>
                Avg Rating: {row['rating_numeric']:.0f}<br>
                Avg Winrate: {row['avg_winrate']:.2f}%
            """,
            color='red',
            fill=True,
            fillColor='red',
            fillOpacity=0.6,
            weight=2
        ).add_to(m)
        
        folium.Marker(
            location=[row['lat'], row['lon']],
            icon=folium.DivIcon(html=f"""
                <div style="font-size: 10pt; color: black; font-weight: bold;">
                    {row['region_code'].upper()}: {row['player_count']}
                </div>
            """)
        ).add_to(m)

m.save('visualizations/region_map.html')
print("✓ Đã tạo biểu đồ: visualizations/region_map.html")

sunburst_data = region_counts.copy()
sunburst_data['world'] = 'World'

fig = px.sunburst(
    sunburst_data,
    path=['world', 'continent', 'region_name'],
    values='player_count',
    color='avg_winrate',
    color_continuous_scale='RdYlGn',
    title='Phân bố người chơi Challenger theo khu vực<br><sub>Sunburst Chart - Interactive</sub>',
    hover_data={'player_count': ':,', 'avg_winrate': ':.2f'}
)

fig.update_traces(
    textinfo='label+percent parent',
    hovertemplate='<b>%{label}</b><br>Players: %{value}<br>Winrate: %{color:.2f}%<extra></extra>'
)

fig.update_layout(
    height=700,
    coloraxis_colorbar=dict(
        title="Avg Winrate (%)",
        ticksuffix="%"
    )
)

fig.write_html('visualizations/region_sunburst.html')
print("✓ Đã tạo biểu đồ: visualizations/region_sunburst.html")

print("\n=== THỐNG KÊ NGƯỜI CHƠI THEO KHU VỰC ===")
print(f"{'Rank':<5} {'Region':<25} {'Code':<8} {'Players':<10} {'Avg WR':<12} {'Avg Rating':<12}")
print("-" * 85)
for idx, row in region_counts.sort_values('player_count', ascending=False).iterrows():
    print(f"{idx+1:<5} {row['region_name']:<25} {row['region_code']:<8} {row['player_count']:<10} "
          f"{row['avg_winrate']:<12.2f} {row['rating_numeric']:<12.0f}")

print(f"\nTổng số người chơi: {region_counts['player_count'].sum()}")
print(f"Số khu vực: {len(region_counts)}")

print("\n=== TOP 5 KHU VỰC ĐÔNG NGƯỜI CHƠI NHẤT ===")
top5 = region_counts.nlargest(5, 'player_count')
for idx, row in top5.iterrows():
    pct = row['player_count'] / region_counts['player_count'].sum() * 100
    print(f"{row['region_name']}: {row['player_count']} ({pct:.1f}%)")

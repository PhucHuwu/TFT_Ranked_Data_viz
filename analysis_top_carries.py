import pandas as pd
import json
import ast
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx
import plotly.graph_objects as go

# Đọc dữ liệu
df = pd.read_csv('data/leaderboard_cleaned.csv')

# Parse JSON data từ topCarries
all_carries = []
character_stats = {}

for carries_str in df['stats.RecentResult.topCarries'].dropna():
    if carries_str and carries_str != '[]':
        try:
            carries = ast.literal_eval(carries_str)
            for carry in carries:
                char_id = carry['character_id'].replace('TFT15_', '')
                count = carry['count']
                avg_place = carry['avg']
                
                all_carries.append(char_id)
                
                if char_id not in character_stats:
                    character_stats[char_id] = {'total_count': 0, 'avg_placements': []}
                
                character_stats[char_id]['total_count'] += count
                character_stats[char_id]['avg_placements'].append(avg_place)
        except:
            continue

# Đếm tần suất
carry_counter = Counter(all_carries)
top_carries = carry_counter.most_common(20)

# Tính avg placement cho mỗi tướng
for char in character_stats:
    character_stats[char]['avg_placement'] = sum(character_stats[char]['avg_placements']) / len(character_stats[char]['avg_placements'])

# === 1. WORDCLOUD ===
wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color='white',
    colormap='plasma',
    relative_scaling=0.5,
    min_font_size=10
).generate_from_frequencies(dict(carry_counter))

plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Tướng Carry Phổ Biến Nhất\n(Kích thước = Tần suất sử dụng)', 
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout(pad=0)
plt.savefig('visualizations/top_carries_wordcloud.png', dpi=300, bbox_inches='tight')
print("✓ Đã tạo biểu đồ: visualizations/top_carries_wordcloud.png")

# === 2. NETWORK GRAPH (Plotly Interactive) ===
# Tạo network graph cho top 15 tướng
top_15_chars = [char for char, _ in top_carries[:15]]

# Tạo graph
G = nx.Graph()

# Thêm nodes (tướng)
for char, count in top_carries[:15]:
    G.add_node(char, size=count, avg_place=character_stats[char]['avg_placement'])

# Tạo edges dựa trên việc xuất hiện cùng nhau trong topCarries
edge_weights = {}
for carries_str in df['stats.RecentResult.topCarries'].dropna():
    if carries_str and carries_str != '[]':
        try:
            carries = ast.literal_eval(carries_str)
            chars = [c['character_id'].replace('TFT15_', '') for c in carries]
            chars = [c for c in chars if c in top_15_chars]
            
            for i in range(len(chars)):
                for j in range(i+1, len(chars)):
                    edge = tuple(sorted([chars[i], chars[j]]))
                    edge_weights[edge] = edge_weights.get(edge, 0) + 1
        except:
            continue

# Thêm edges với trọng số > 2
for edge, weight in edge_weights.items():
    if weight > 2:
        G.add_edge(edge[0], edge[1], weight=weight)

# Tạo layout
pos = nx.spring_layout(G, k=2, iterations=50)

# Tạo edge traces
edge_trace = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    weight = G.edges[edge]['weight']
    edge_trace.append(
        go.Scatter(
            x=[x0, x1, None],
            y=[y0, y1, None],
            mode='lines',
            line=dict(width=weight/2, color='rgba(125, 125, 125, 0.3)'),
            hoverinfo='none',
            showlegend=False
        )
    )

# Tạo node trace
node_x = []
node_y = []
node_size = []
node_color = []
node_text = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    size = G.nodes[node]['size']
    avg_place = G.nodes[node]['avg_place']
    node_size.append(size * 2)
    node_color.append(avg_place)
    node_text.append(f"{node}<br>Picks: {size}<br>Avg Place: {avg_place:.2f}")

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=[node for node in G.nodes()],
    textposition="top center",
    hovertext=node_text,
    hoverinfo='text',
    marker=dict(
        size=node_size,
        color=node_color,
        colorscale='RdYlGn_r',
        showscale=True,
        colorbar=dict(
            title="Avg<br>Placement",
            thickness=15,
            xanchor='left',
            title_side='right'
        ),
        line=dict(width=2, color='white')
    ),
    showlegend=False
)

# Tạo figure
fig = go.Figure(data=edge_trace + [node_trace])

fig.update_layout(
    title='Network Graph - Mối quan hệ giữa các tướng Carry<br><sub>Kích thước node = Số lần pick | Màu = Avg Placement | Độ dày đường = Xuất hiện cùng nhau</sub>',
    showlegend=False,
    hovermode='closest',
    margin=dict(b=20, l=5, r=5, t=80),
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    height=700,
    plot_bgcolor='rgba(240, 240, 240, 0.5)'
)

fig.write_html('visualizations/top_carries_network.html')
print("✓ Đã tạo biểu đồ: visualizations/top_carries_network.html")

# Thống kê
print("\n=== TOP 20 TƯỚNG CARRY PHỔ BIẾN ===")
print(f"{'Rank':<5} {'Champion':<20} {'Picks':<10} {'Avg Placement':<15}")
print("-" * 50)
for i, (char, count) in enumerate(top_carries, 1):
    avg_place = character_stats[char]['avg_placement']
    print(f"{i:<5} {char:<20} {count:<10} {avg_place:<15.2f}")

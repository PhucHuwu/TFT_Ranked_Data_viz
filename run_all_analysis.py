"""
Master Script - Chạy tất cả các phân tích TFT Ranked Data
Thực hiện 6 loại thống kê và tạo biểu đồ trực quan
"""

import os
import sys
from datetime import datetime

def run_analysis(script_name, description):
    """Chạy một script phân tích"""
    print("\n" + "="*70)
    print(f"ĐANG CHẠY: {description}")
    print("="*70)
    try:
        exec(open(script_name, encoding='utf-8').read(), {'__name__': '__main__'})
        print(f"✅ Hoàn thành: {description}")
        return True
    except Exception as e:
        print(f"❌ Lỗi khi chạy {script_name}: {str(e)}")
        return False

def main():
    print("="*70)
    print("TFT RANKED DATA ANALYSIS - COMPREHENSIVE STATISTICS")
    print("="*70)
    print(f"Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Tạo thư mục visualizations nếu chưa có
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')
        print("✓ Đã tạo thư mục 'visualizations'")
    
    # Danh sách các phân tích
    analyses = [
        {
            'script': 'analysis_item_data.py',
            'description': '1. Thống kê ItemData (AD, AP, Tank) - Treemap'
        },
        {
            'script': 'analysis_avg_similarity.py',
            'description': '2. Thống kê Độ Flexible (avg_similarity) - Histogram + Boxplot'
        },
        {
            'script': 'analysis_top_carries.py',
            'description': '3. Thống kê Top Carries - WordCloud + Network Graph'
        },
        {
            'script': 'analysis_playstyle.py',
            'description': '4. Thống kê Playstyle (Eco vs High Tempo) - Scatter + Regression'
        },
        {
            'script': 'analysis_region.py',
            'description': '5. Thống kê Người chơi theo Region - Map + Sunburst'
        },
        {
            'script': 'analysis_performance.py',
            'description': '6. Thống kê Performance (Winrate & Placement) - Heatmap + Violin'
        }
    ]
    
    # Chạy từng phân tích
    results = []
    for analysis in analyses:
        success = run_analysis(analysis['script'], analysis['description'])
        results.append({
            'name': analysis['description'],
            'success': success
        })
    
    # Tổng kết
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    
    successful = sum(1 for r in results if r['success'])
    total = len(results)
    
    print(f"\nĐã hoàn thành: {successful}/{total} phân tích")
    print("\nChi tiết:")
    for i, result in enumerate(results, 1):
        status = "✅" if result['success'] else "❌"
        print(f"{status} {result['name']}")
    
    print("\n" + "="*70)
    print("CÁC FILE BIỂU ĐỒ ĐÃ TẠO (trong thư mục visualizations/):")
    print("="*70)
    
    viz_files = [
        ("item_data_treemap.html", "Treemap - Phân bố trang bị (Plotly Interactive)"),
        ("avg_similarity_distribution.html", "Histogram + Boxplot - Độ flexible (Plotly Interactive)"),
        ("top_carries_wordcloud.png", "WordCloud - Tướng carry phổ biến"),
        ("top_carries_network.html", "Network Graph - Mối quan hệ tướng (Plotly Interactive)"),
        ("playstyle_scatter.html", "Scatter + Regression - Phong cách chơi (Plotly Interactive)"),
        ("region_map.html", "Map - Phân bố người chơi theo khu vực (Folium)"),
        ("region_sunburst.html", "Sunburst - Phân bố theo châu lục (Plotly Interactive)"),
        ("performance_heatmap.html", "Heatmap - Tương quan metrics (Plotly Interactive)"),
        ("performance_violin.html", "Violin Plot - Phân tích performance (Plotly Interactive)")
    ]
    
    for filename, description in viz_files:
        filepath = os.path.join('visualizations', filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"  ✓ {filename:<35} - {description}")
        else:
            print(f"  ✗ {filename:<35} - (Chưa tạo)")
    
    print("\n" + "="*70)
    print("BIỂU ĐỒ TƯƠNG TÁC (Interactive Charts):")
    print("="*70)
    print("  1. Treemap (Item Data)")
    print("  2. Histogram + Boxplot (Avg Similarity)")
    print("  3. Network Graph (Top Carries)")
    print("  4. Scatter + Regression (Playstyle)")
    print("  5. Sunburst (Region)")
    print("  6. Heatmap (Performance Correlation)")
    print("  7. Violin Plot (Performance Distribution)")
    print("\n  => Tổng cộng: 7 biểu đồ tương tác (Plotly/Folium)")
    
    print("\n" + "="*70)
    print(f"Thời gian kết thúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

if __name__ == "__main__":
    main()

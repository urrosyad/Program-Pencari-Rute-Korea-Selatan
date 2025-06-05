import networkx as nx
import matplotlib.pyplot as plt
import math

# Data kota dan posisi fiktif (untuk heuristik A*)
city_coords = {
    "Seoul": (0, 0),
    "Busan": (8, -8),
    "Incheon": (-1, 0),
    "Daegu": (6, -5),
    "Daejeon": (3, -2),
    "Gwangju": (0, -6),
    "Suwon": (1, -1),
    "Ulsan": (8, -6),
    "Changwon": (7, -7),
    "Jeonju": (1, -4)
}

# Daftar edge dan jaraknya (berdasarkan input user sebelumnya)
edges = [
    ("Seoul", "Incheon", 30), ("Seoul", "Daejeon", 140), ("Seoul", "Suwon", 35),
    ("Seoul", "Jeonju", 195), ("Seoul", "Daegu", 280), ("Incheon", "Suwon", 50),
    ("Incheon", "Daejeon", 160), ("Daejeon", "Daegu", 150), ("Daejeon", "Jeonju", 70),
    ("Jeonju", "Gwangju", 95), ("Daegu", "Busan", 90), ("Daegu", "Ulsan", 100),
    ("Daegu", "Changwon", 130), ("Busan", "Ulsan", 70), ("Busan", "Changwon", 40),
    ("Gwangju", "Jeonju", 90), ("Gwangju", "Daejeon", 150), ("Gwangju", "Changwon", 220),
    ("Suwon", "Daejeon", 115), ("Suwon", "Daegu", 270), ("Incheon", "Jeonju", 210),
    ("Suwon", "Gwangju", 330), ("Ulsan", "Changwon", 90), ("Busan", "Jeonju", 280),
    ("Daegu", "Gwangju", 240), ("Daejeon", "Busan", 250), ("Changwon", "Jeonju", 240),
    ("Incheon", "Gwangju", 310), ("Seoul", "Changwon", 385), ("Incheon", "Busan", 400)
]

# Membuat graf dan menambahkan edge dan node
G = nx.Graph()
for city, coord in city_coords.items():
            G.add_node(city, pos=coord)
for u, v, dist in edges:
            G.add_edge(u, v, weight=dist)

# Fungsi heuristik menggunakan jarak Euclidean (digunakan oleh A*)
def heuristic(a, b):
    ax, ay = city_coords[a]
    bx, by = city_coords[b]
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

# Pilih kota asal dan tujuan
print("Daftar kota yang tersedia:", ', '.join(city_coords.keys()))
start = input("Masukkan kota awal: ").strip().title()
goal = input("Masukkan kota tujuan: ").strip().title()

# A* untuk mencari jalur terpendek dari start ke goal
path = nx.astar_path(G, start, goal, heuristic=heuristic, weight='weight')
total_distance = nx.path_weight(G, path, weight='weight')

# Visualisasi graf + jalur merah
pos = city_coords
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']} km" for u, v, d in G.edges(data=True)})
edge_path = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='red', width=3)

# Menampilkan visualisasi graf dari seluruh kota dan rutenya
plt.title(f"Rute A* dari {start} ke {goal} (Total: {total_distance} km)")
plt.axis('off')
plt.tight_layout()
plt.show()

# Cetak hasil
print(f"Rute terpendek: {' → '.join(path)}")
print(f"Total jarak: {total_distance} km")

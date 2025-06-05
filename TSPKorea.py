import networkx as nx
import itertools

# Daftar kota-kota besar di Korea Selatan
cities = [
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon",
    "Gwangju", "Suwon", "Ulsan", "Changwon", "Jeonju"
]

# Rute antar kota dan jarak tempuh (km)
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

# Buat graf tak berarah
G = nx.Graph()
G.add_nodes_from(cities)
for u, v, d in edges:
    G.add_edge(u, v, weight=d)

# Fungsi untuk menghitung total jarak sebuah rute
def calculate_total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        if G.has_edge(u, v):
            total += G[u][v]['weight']
        else:
            return float('inf')  # Jika tidak ada edge, anggap tak terhubung
    return total

# TSP brute-force: semua kemungkinan permutasi kota
best_route = None
min_distance = float('inf')

# Kita mulai dari kota pertama (Seoul), lalu permutasi sisanya
start_city = cities[0]
other_cities = cities[1:]

# Cek semua permutasi kota yang tersisa
for perm in itertools.permutations(other_cities):
    route = [start_city] + list(perm) + [start_city]  # kembali ke kota awal
    total_distance = calculate_total_distance(route)
    if total_distance < min_distance:
        min_distance = total_distance
        best_route = route

# Tampilkan hasil
print("\nRute TSP terbaik:")
print(" → ".join(best_route))
print(f"Total jarak tempuh: {min_distance} km")

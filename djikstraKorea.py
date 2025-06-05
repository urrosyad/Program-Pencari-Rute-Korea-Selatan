import networkx as nx  # Untuk membuat dan mengelola struktur graf
import matplotlib.pyplot as plt  # Untuk visualisasi graf

# Daftar kota-kota besar (simpul/vertex)
cities = [
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon",
    "Gwangju", "Suwon", "Ulsan", "Changwon", "Jeonju"
]

# Daftar rute antar kota dengan bobot jarak dalam kilometer
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

# Membuat objek graf tak berarah
G = nx.Graph()

# Menambahkan semua kota sebagai simpul
G.add_nodes_from(cities)

# Menambahkan sisi dengan atribut jarak sebagai bobot
for u, v, distance in edges:
    G.add_edge(u, v, weight=distance) 
     # 'weight' akan digunakan oleh algoritma Dijkstra

# Menampilkan daftar kota yang tersedia
print("#=============== MAU KEMANA?: ===============#")
for city in cities:
    print(":::::::::::::::     ", city, "\t:::::::::::::::::")

# Input kota asal dan tujuan dari pengguna
source = input("\nMasukkan nama kota asal: ").strip().title()  # Mengubah input menjadi format kapitalisasi yang benar
target = input("Masukkan nama kota tujuan: ").strip().title()

# Validasi apakah kota ada dalam daftar
if source not in cities or target not in cities:
    print("\nKota tidak ditemukan dalam daftar. Pastikan penulisan sudah benar.")
else:
    try:
        shortest_path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
        total_distance = nx.dijkstra_path_length(G, source=source, target=target, weight='weight')

        # Tampilkan hasil
        print("\nJalur tercepat:")
        print(" → ".join(shortest_path))
        print("Total jarak ditempuh:", total_distance, "km")
    except nx.NetworkXNoPath:
        print(f"\nTidak ada jalur itu yang menghubungkan {source} ke {target}.\n")

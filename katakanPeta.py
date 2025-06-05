import networkx as nx           # untuk membuat dan memanipulasi graf
import matplotlib.pyplot as plt # untuk visualisasi graf

# Daftar vertex (kota-kota besar di Korea)
# Membuat daftar simpul (kota)
cities = [
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon",
    "Gwangju", "Suwon", "Ulsan", "Changwon", "Jeonju"
]  

# Daftar edge (rute antar kota) beserta bobot jarak dalam kilometer
# Membuat daftar sisi yang menyambungkan kota-kota beserta bobot jaraknya (dalam km)
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

# Rumus mencari waktu tempuh = jarak / kecepatan × 60 menit
def calc_travel_time(km):
    return round((km / 80) * 60)  # Fungsi untuk menghitung waktu tempuh dalam menit

# Buat graf 
G = nx.Graph() 

# Menambahkan semua kota ke dalam graf sebagai simpul
G.add_nodes_from(cities)  

# Tambahkan edge dengan jarak dan waktu tempuh
for u, v, distance in edges:
    time = calc_travel_time(distance) # Hitung waktu tempuh dari jarak
    G.add_edge(u, v, distance=distance, time=time) # Tambahkan rute antar kota dengan atribut jarak dan waktu

# Membuat Posisi kota agar tidak acak (layout)
pos = nx.spring_layout(G, seed=42)  

# Memvisualisasikan graf
plt.figure(figsize=(15, 10))  # Mengatur ukuran gambar
nx.draw(
    G, pos, with_labels=True, node_color='skyblue',
    node_size=2000, font_size=10, font_weight='bold', edge_color='gray' )  # Gambar graf dengan label, warna, dan ukuran simpul

# Buat label untuk edge dengan jarak dan waktu tempuh
edge_labels = {
    (u, v): f"{d['distance']} km\n{d['time']} min"
    for u, v, d in G.edges(data=True)
}  

# Gambar label pada sisi graf
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)  

plt.title("Visualisasi Graf Kota-Kota di Korea dengan Jarak dan Waktu Tempuh (Mobil)", fontsize=14)  # Judul grafik
plt.axis('off')       # Hilangkan sumbu x dan y
plt.tight_layout()    # Atur layout agar tidak terpotong
plt.show()            # Tampilkan visualisasi graf

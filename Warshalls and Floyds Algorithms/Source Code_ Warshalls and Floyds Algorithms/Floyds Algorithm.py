def floyd(matriks_adj):
    n = len(matriks_adj)

    # Inisialisasi matriks jarak dengan matriks ketetanggaan awal
    jarak = [row[:] for row in matriks_adj]

    # Iterasi untuk mencari jarak terpendek antara setiap pasangan simpul
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Perbarui matriks jarak untuk mencatat jarak terpendek
                jarak[i][j] = min(jarak[i][j], jarak[i][k] + jarak[k][j])

    return jarak


graf = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

# Panggil fungsi Floyd
hasil = floyd(graf)

# Cetak hasil
for baris in hasil:
    print(baris)

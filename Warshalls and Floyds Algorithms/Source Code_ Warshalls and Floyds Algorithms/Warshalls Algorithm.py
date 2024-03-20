def warshall(matriks_ketetanggaan):
    n = len(matriks_ketetanggaan)

    # Inisialisasi matriks transitif dengan matriks ketetanggaan awal
    matriks_transitif = [list(row) for row in matriks_ketetanggaan]

    # Iterasi untuk mencari jalur terpendek antara setiap pasangan simpul
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Perbarui matriks transitif untuk mencatat jalur terpendek
                matriks_transitif[i][j] = matriks_transitif[i][j] or (matriks_transitif[i][k] and matriks_transitif[k][j])

    return matriks_transitif

# Contoh penggunaan
graf = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

hasil = warshall(graf)
for baris in hasil:
    print(baris)

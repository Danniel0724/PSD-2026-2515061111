def binary_search(arr, target):
    awal = 0
    akhir = len(arr) - 1

    while awal <= akhir:
        tengah = (awal + akhir) // 2

        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            awal = tengah + 1
        else:
            akhir = tengah - 1

    return -1

data = []
jumlah = int(input("Masukkan jumlah nomor buku: "))

for i in range(jumlah):
    nomor = int(input("Masukkan nomor buku secara urut: "))
    data.append(nomor)

cari = int(input("Masukkan nomor buku yang dicari: "))

hasil = binary_search(data, cari)

if hasil != -1:
    print("Nomor buku ditemukan pada indeks", hasil)
else:
    print("Nomor buku tidak ditemukan")
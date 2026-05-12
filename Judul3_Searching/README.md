Tugas Akhir Judul 3 

Judul = Mencari Nomor Buku menggunakan BinarySearch

Binary Search digunakan karena proses pencariannya lebih cepat dan efisien dibandingkan pencarian biasa (Linear Search), terutama jika jumlah data sangat banyak. Karena data sudah terurut, Binary Search bisa langsung memeriksa nilai tengah, lalu menentukan apakah pencarian dilanjutkan ke kiri atau ke kanan.

<img width="364" height="317" alt="Screenshot 2026-05-12 223423" src="https://github.com/user-attachments/assets/0ffb85b1-a625-44fb-a01c-0888077f0cbd" />

def binary_search(arr, target):
Membuat fungsi binary search untuk mencari nomor buku.

awal = 0
Menentukan indeks awal pencarian.

akhir = len(arr) - 1
Menentukan indeks akhir pencarian.

while awal <= akhir:
Melakukan perulangan selama area pencarian masih tersedia.

tengah = (awal + akhir) // 2
Menentukan posisi tengah data.

if arr[tengah] == target:
Mengecek apakah nomor buku di tengah sama dengan nomor yang dicari.

return tengah
Mengembalikan indeks jika data ditemukan.

elif arr[tengah] < target:
Jika nilai tengah lebih kecil dari target.

awal = tengah + 1
Pencarian digeser ke bagian kanan.

else:
Jika nilai tengah lebih besar dari target.

akhir = tengah - 1
Pencarian digeser ke bagian kiri.

return -1
Mengembalikan nilai -1 jika data tidak ditemukan.

data = []
Membuat list kosong untuk menyimpan nomor buku.

jumlah = int(input(...))
Meminta jumlah nomor buku.

for i in range(jumlah):
Perulangan untuk input data.

nomor = int(input(...))
Meminta input nomor buku.

data.append(nomor)
Menambahkan nomor buku ke list.

cari = int(input(...))
Meminta nomor buku yang dicari.

hasil = binary_search(data, cari)
Menjalankan proses pencarian.

if hasil != -1:
Mengecek apakah data ditemukan.

print("Nomor buku ditemukan...")
Menampilkan posisi buku jika ditemukan.

else:
Jika data tidak ditemukan.
print("Nomor buku tidak ditemukan")
Menampilkan pesan jika buku tidak ada.

Output : 
<img width="476" height="106" alt="Screenshot 2026-05-12 223405" src="https://github.com/user-attachments/assets/66acc51f-4359-4ec2-8990-8ffde3e46553" />
memasukkan angkanya secara berurutan, lalu kita memilih angka yang ingin kita pilih, dan setelah dipilih akan muncul angka tersebut di indeks ke berapa.

Link Youtube : https://youtu.be/UGeSXrOzc34

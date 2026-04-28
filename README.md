Judul : Sistem Absensi Mahasiswa 

program ini berfungsi untuk mengelola data kehadiran mahasiswa secara sederhana, user dapat memasukan data(absen/Hadir) dalam bentuk tabel dan juga bisa menghitung total kehadiran mahasiswa 

Algoritma dan struktur data yang diterapkan dalam program ini adalah struktur data matriks (list 2 dimensi) yang digunakan untuk menyimpan data absensi, di mana baris merepresentasikan mahasiswa dan kolom merepresentasikan hari. Selain itu, program juga menggunakan algoritma perulangan (looping) seperti for dan while untuk mengakses serta memproses data, serta percabangan (if-elif-else)

Source code : <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/2a756dc5-b80d-4dab-b50c-917aee53c9e9" />

def menu(): Mendefinisikan fungsi menu
print("\n=== SISTEM ABSENSI SISWA ===") = Menampilkan judul program
print("1. Tampilkan Absensi") = Menampilkan pilihan menu 1
print("2. Input Absensi") = Menampilkan pilihan menu 2
print("3. Hitung Kehadiran") = Menampilkan pilihan menu 3
print("0. Keluar") = Menampilkan pilihan keluar

absensi = [[0,0,0],[0,0,0]] = Membuat matrix 2D (data absensi)
hari = ["Senin","Selasa","Rabu"] = Menyimpan nama hari

while True: = Loop program terus berjalan
menu() = Menampilkan menu
pilih = input("Pilih menu: ") = Menerima input user

if pilih == "1": = Jika pilih tampilkan data
elif pilih == "2": = Jika pilih input data
elif pilih == "3": = Jika pilih hitung data
elif pilih == "0": = Jika pilih keluar
else: = Jika input tidak valid

Output : <img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/bb632d2d-17f0-4683-8ab8-99095da0d61d" />

=== SISTEM ABSENSI SISWA === = Menampilkan judul program
1. Tampilkan Absensi = Pilihan untuk melihat data
2. Input Absensi = Pilihan untuk mengisi data
3. Hitung Kehadiran = Pilihan untuk menghitung total
0. Keluar = Pilihan untuk keluar dari program

Input absensi Siswa 1 = Menunjukkan data yang diinput untuk siswa ke-1
Senin (1=Hadir, 0=Tidak): = Input hari Senin
Selasa (1=Hadir, 0=Tidak): = Input hari Selasa
Rabu (1=Hadir, 0=Tidak): = Input hari Rabu
Input absensi Siswa 2 = Menunjukkan data siswa ke-2
(diulang sama seperti siswa 1) = karena menggunakan perulangan

=== DATA ABSENSI === = Judul tampilan data
Siswa Senin Selasa Rabu = Header tabel
1 1 0 1 = Data siswa 1 (hadir/tidak per hari)
2 1 1 0 = Data siswa 2

=== TOTAL KEHADIRAN === = Judul hasil
Siswa 1 hadir = 2 hari = Total hadir siswa 1
Siswa 2 hadir = 2 hari = Total hadir siswa 2

Program selesai = Menandakan program berhenti

LINK : [https://youtu.be/nj-aF_Ltsy0](url)



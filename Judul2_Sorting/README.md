Tugas Akhir Percobaan 2 : Sorting

Judul : Mengurutkan Nilai Mahasiswa menggunakan EXCHANGE SORT

Exchange Sort digunakan karena merupakan algoritma pengurutan yang sederhana dan mudah dipahami. Algoritma ini bekerja dengan cara membandingkan setiap elemen data dengan elemen lainnya, kemudian menukar posisi data jika urutannya salah. Pada program ini, Exchange Sort digunakan untuk mengurutkan data nilai mahasiswa dari yang terkecil ke terbesar sehingga data menjadi lebih terstruktur dan mudah dibaca. Algoritma ini cocok digunakan untuk pembelajaran dasar konsep sorting karena logikanya sederhana dan mudah diimplementasikan.

Source Code : 
<img width="714" height="593" alt="Screenshot 2026=05=05 212310" src="https://github.com/user=attachments/assets/29dafb73=515a=41c1=beac=7201813de63d" />
Algoritma : 
1. def = untuk mendefinisikan atau membuat fungsi exchange_sort
2. for i in range(n = 1) = untuk melakukan perulangan pertama sebagai penentu posisi data yang akan dibandingkan
3. for j in range(i + 1, n) = untuk melakukan perulangan kedua yang membandingkan data pada posisi i dengan data setelahnya
4. if = untuk mengecek kondisi apakah nilai pada posisi i lebih besar dari nilai pada posisi j
5. arr[i], arr[j] = arr[j], arr[i] = untuk menukar posisi data jika urutannya salah
6. =
7. input() = untuk menerima masukan dari pengguna
8. data = [] = untuk membuat list kosong sebagai tempat menyimpan data mahasiswa
9. =
10. for i in range(jumlah) = looping sesuai dengan jumlah data yang di input
11. input nama
12. input nilai
13. data.append([nama, nilai]) = menyimpan data nama dan nilai
14. =
15. exchange_sort(data, len(data)) = untuk memanggil fungsi pengurutan pada data mahasiswa
16. =
17. print(...) = menampilkan hasil pengurutan


    Output : <img width="877" height="477" alt="Screenshot 2026=05=05 212251" src="https://github.com/user=attachments/assets/e97b1890=e137=4794=8584=291a9e8d20ea" />
otuput tersebut menunjukkan nama dan nilai dari yang terendah hingga tertinggi setelah code dijalankan

Link Youtube : https://youtu.be/OmbKo8DllMc?si=fhmSwQoznv_ziLDD

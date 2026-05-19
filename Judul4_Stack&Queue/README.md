Tugas Akhir Judul 4

Judul : Antrian Kantin menggunakan Queue Array

disini saya menggunakan Queue Array untuk antrian kantin karena sistem ini sangat sesuai dengan cara kerja antrian di kehidupan nyata, yaitu menggunakan prinsip FIFO (First In First Out), Siapa yang datang lebih dulu, akan dilayani lebih dulu

<img width="494" height="401" alt="Screenshot 2026-05-19 222444" src="https://github.com/user-attachments/assets/cfe8d738-2f27-4997-9598-05a5fea11a30" />
<img width="624" height="319" alt="Screenshot 2026-05-19 222434" src="https://github.com/user-attachments/assets/87a4cb28-974d-40c2-b5e7-6f60e6e6e924" />

1. class QueueArray:
Membuat class bernama QueueArray sebagai struktur dasar antrian

2. def __init__(self):
Method otomatis dijalankan saat objek dibuat

3. self.queue = []
Membuat list kosong untuk menyimpan data antrian

4. def enqueue(self, item):
Method untuk menambahkan data ke antrian

5. self.queue.append(item)
Menambahkan data ke bagian belakang antrian

6. print(item, "masuk ke antrian")
Menampilkan pesan bahwa data berhasil masuk

7. def dequeue(self):
Method untuk menghapus data dari depan antrian

8. if len(self.queue) == 0:
Mengecek apakah antrian kosong

9. print("Antrian kosong")
Menampilkan pesan jika tidak ada data

10. else:
Jika antrian tidak kosong

11. print(self.queue.pop(0), "sedang dilayani")
Menghapus data pertama dan menampilkan siapa yang sedang dilayani

12. def peek(self):
Method untuk melihat data terdepan tanpa menghapusnya

13. if len(self.queue) == 0:
Mengecek apakah antrian kosong

14. print("Antrian kosong")
Menampilkan pesan jika kosong

15. else:
Jika ada data

16. print("Antrian terdepan:", self.queue[0])
Menampilkan data paling depan

17. def display(self):
Method untuk menampilkan seluruh isi antrian

18. if len(self.queue) == 0:
Mengecek apakah antrian kosong

19. print("Antrian kosong")
Menampilkan pesan jika kosong

20. else:
Jika antrian berisi data

21. print("Isi antrian:", self.queue)
Menampilkan seluruh isi antrian

22. def main():
Fungsi utama program

23. queue = QueueArray()
Membuat objek queue dari class QueueArray.

24. pilih = 0
ntuk menyimpan pilihan menu

25. while pilih != 5:
Perulangan berjalan sampai user memilih keluar

26. print("\n=== PROGRAM QUEUE ARRAY ===")
Menampilkan judul program

28. print("1. Enqueue (Tambah Antrian)")
Menampilkan menu tambah antrian

29. print("2. Dequeue (Layani Antrian)")
Menampilkan menu melayani antrian

30. print("3. Peek (Lihat Antrian Depan)")
Menampilkan menu melihat antrian depan

31. print("4. Display (Tampilkan Antrian)")
Menampilkan menu menampilkan semua antrian

32. print("5. Keluar")
Menampilkan menu keluar

33. try:
Mencoba menjalankan input user

34. pilih = int(input("Pilih menu: "))
Menerima input angka dari user

35. except ValueError:
Menangani kesalahan jika input bukan angka

36. print("Input tidak valid!")
Menampilkan pesan error

37. continue
Mengulang kembali ke menu

38. if pilih == 1:
Jika user memilih menu tambah antrian

39. nama = input("Masukkan nama mahasiswa: ")
Meminta input nama mahasiswa

40. queue.enqueue(nama)
Memasukkan nama ke antrian

41. elif pilih == 2:
Jika user memilih menu layani antrian

42. queue.dequeue()
Menghapus antrian terdepan

43. elif pilih == 3:
Jika user memilih menu lihat antrian depan

44. queue.peek()
Menampilkan antrian terdepan

45. elif pilih == 4:
Jika user memilih menu tampilkan antrian

46. queue.display()
Menampilkan seluruh isi antrian

47. elif pilih == 5:
Jika user memilih keluar

48. print("Program selesai.")
Menampilkan pesan program selesai

49. else:
Jika input menu tidak sesuai

50. print("Pilihan tidak valid")
Menampilkan pesan pilihan salah

51. main()
Menjalankan fungsi utama program


OUTPUT : <img width="293" height="416" alt="Screenshot 2026-05-19 222423" src="https://github.com/user-attachments/assets/6444a3aa-8d65-4c7e-8958-1857d2bd816c" />
<img width="280" height="412" alt="Screenshot 2026-05-19 222409" src="https://github.com/user-attachments/assets/ea765078-1d66-45de-a476-f2d4ae9497e7" />

intput angka berurut, lalu masukan beberapa nama mahasiswa untuk sebagai contoh, nanti kita bisa melihat antrian dan siapa yang sedang dilayani, lalu jika kita input selain angka 1-5, program akan eror dan mengulang kembali ke pilihan.


Link Youtube : https://youtu.be/pvd208aSn-o

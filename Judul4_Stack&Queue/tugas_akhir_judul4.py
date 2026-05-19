class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "masuk ke antrian")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Antrian kosong")
        else:
            print(self.queue.pop(0), "sedang dilayani")

    def peek(self):
        if len(self.queue) == 0:
            print("Antrian kosong")
        else:
            print("Antrian terdepan:", self.queue[0])

    def display(self):
        if len(self.queue) == 0:
            print("Antrian kosong")
        else:
            print("Isi antrian:", self.queue)


def main():
    queue = QueueArray()
    pilih = 0

    while pilih != 5:
        print("\n=== ANTRIAN KANTIN ===")
        print("1. Tambah Antrian")
        print("2. Layani Antrian")
        print("3. Lihat Antrian Depan")
        print("4. Tampilkan Antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama mahasiswa: ")
            queue.enqueue(nama)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
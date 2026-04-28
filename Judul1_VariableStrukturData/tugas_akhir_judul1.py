def menu():
    print("\n=== SISTEM ABSENSI MAHASISWA ===")
    print("1. Tampilkan Absensi")
    print("2. Input Absensi")
    print("3. Hitung Kehadiran")
    print("0. Keluar")


absensi = [
    [0, 0, 0],
    [0, 0, 0]
]

hari = ["Senin", "Selasa", "Rabu"]


while True:
    menu()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        print("\n=== DATA ABSENSI ===")
        print("Siswa   Senin   Selasa   Rabu")

        for i in range(len(absensi)):
            print(f"{i+1}       {absensi[i][0]}        {absensi[i][1]}        {absensi[i][2]}")

    elif pilih == "2":
        for i in range(len(absensi)):
            print(f"\nInput absensi Mahasiswa {i+1}")
            for j in range(len(hari)):
                print(f"{hari[j]} (1=Hadir, 0=Tidak): ", end="")
                absensi[i][j] = int(input())

    elif pilih == "3":
        print("\n=== TOTAL KEHADIRAN ===")
        for i in range(len(absensi)):
            total = sum(absensi[i])
            print(f"Mahasiswa {i+1} hadir = {total} hari")

    elif pilih == "0":
        print("Program selesai")
        break

    else:
        print("Menu tidak ada!")
def exchange_sort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]

jumlah = int(input("Masukkan jumlah mahasiswa: "))
data = []

for i in range(jumlah):
    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai: "))
    data.append([nama, nilai])

exchange_sort(data, len(data))

print("\nHasil setelah diurutkan berdasarkan nilai:")
for mahasiswa in data:
    print(mahasiswa[0], "-", mahasiswa[1])
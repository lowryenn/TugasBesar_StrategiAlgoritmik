def main():
    while True:
        n = int(input("Masukkan jumlah barang (min 8): "))
        if n >= 8:
            break
        else:
            print("Jumlah barang minimal 8! Coba lagi.\n")

    nama = [""] * n
    berat = [0] * n
    profit = [0] * n

    for i in range(n):
        print("Barang ke-", i+1)
        nama[i] = input("Nama: ")
        berat[i] = int(input("Berat: "))
        profit[i] = int(input("Profit: "))

    while True:
        W = int(input("Masukkan kapasitas knapsack: "))
        if (W > 0):
            break
        else:
            print("Kapasitas harus lebih dari 0!")

    print("TABEL BARANG")
    print("No  Nama   Berat   Profit")
    for i in range(n):
        print(i+1, nama[i], berat[i], profit[i])

    print("Kapasitas:", W)


if __name__ == "__main__":
    main()
def input_barang():
    while True:
        n = int(input("Masukkan jumlah barang (minimal 8): "))
        if n >= 8:
            break
        print("Jumlah barang harus minimal 8!")

    nama = []
    berat = []
    profit = []

    for i in range(n):
        print(f"\nBarang ke-{i+1}")

        nama.append(input("Nama Barang : "))
        berat.append(int(input("Berat       : ")))
        profit.append(int(input("Profit      : ")))

    while True:
        kapasitas = int(input("\nMasukkan kapasitas knapsack : "))
        if kapasitas > 0:
            break
        print("Kapasitas harus lebih dari 0!")

    return n, nama, berat, profit, kapasitas
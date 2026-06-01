def tampil_tabel(nama, berat, profit):

    print("\n===== DATA BARANG =====")

    print(f"{'No':<5}{'Nama':<15}{'Berat':<10}{'Profit':<10}")

    for i in range(len(nama)):
        print(
            f"{i+1:<5}"
            f"{nama[i]:<15}"
            f"{berat[i]:<10}"
            f"{profit[i]:<10}"
        )
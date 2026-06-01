import time

from input_handler import input_barang
from display import tampil_tabel
from statistics import tampil_statistik

import knapsack


def main():

    n, nama, berat, profit, kapasitas = input_barang()

    tampil_tabel(
        nama,
        berat,
        profit
    )

    print("\n===== PROSES DFS =====")

    start = time.perf_counter()

    knapsack.reset()

    knapsack.dfs(
        0,
        n,
        berat,
        profit,
        kapasitas,
        0,
        0,
        [],
        nama
    )

    end = time.perf_counter()

    best_profit, best_solution, node_count = (
        knapsack.hasil()
    )

    print("\n===== SOLUSI OPTIMAL =====")

    total_berat = 0

    for idx in best_solution:

        print(
            nama[idx],
            "- Berat:",
            berat[idx],
            "- Profit:",
            profit[idx]
        )

        total_berat += berat[idx]

    print("\nTotal Berat :", total_berat)
    print("Total Profit:", best_profit)

    tampil_statistik(
        node_count,
        end - start
    )


if __name__ == "__main__":
    main()
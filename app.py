# app.py
from flask import Flask, render_template, request
import time
import copy

# Import fungsi solver DFS + Branch and Bound dari folder algorithms
from algorithms.dfs_solver import solve_knapsack

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    start_time = time.perf_counter()

    try:
        capacity = int(request.form["capacity"])
    except (ValueError, KeyError):
        return "Kapasitas harus berupa angka valid.", 400

    # VALIDASI TEGAS: Mencegah kapasitas minus masuk ke algoritma
    if capacity < 0:
        return "Error: Kapasitas knapsack tidak boleh bernilai negatif!", 400

    items = []
    # Mengambil data 8 barang dari form input
    for i in range(8):
        nama = request.form.get(f"nama{i}", f"Barang {i+1}")
        
        try:
            berat = int(request.form.get(f"berat{i}", 0))
            profit = int(request.form.get(f"profit{i}", 0))
        except ValueError:
            return f"Berat dan profit untuk barang ke-{i+1} harus berupa angka.", 400

        # Validasi tambahan untuk barang
        if berat <= 0:
            return f"Error: Berat {nama} harus lebih besar dari 0!", 400
        if profit < 0:
            return f"Error: Profit {nama} tidak boleh bernilai negatif!", 400

        items.append({
            "nama": nama,
            "berat": berat,
            "profit": profit
        })

    # MODIFIKASI: Lakukan deepcopy agar data awal untuk tabel input dosen tidak ikut teracak/ter-sort oleh algoritma
    items_input_backup = copy.deepcopy(items)

    # PANGGIL SOLVER DFS + BRANCH AND BOUND
    result = solve_knapsack(items, capacity)

    end_time = time.perf_counter()
    execution_time = round(end_time - start_time, 6)

    return render_template(
        "result.html",
        selected_items=result["selected_items"],
        best_profit=result["best_profit"],
        total_weight=result["total_weight"],
        node_count=result["node_count"],
        explored_nodes=result["explored_nodes"],
        execution_time=execution_time,
        capacity=capacity,
        items_input=items_input_backup  # Dikirim ke HTML untuk memenangi poin "Tabel barang input"
    )

if __name__ == "__main__":
    app.run(debug=True)
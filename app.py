from flask import Flask, render_template, request
import time
import copy

from algorithms.dfs_solver import solve_knapsack

app = Flask(__name__)

@app.route("/")
def home():
    # PERBAIKAN: Indentasi fungsi harus masuk ke dalam
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():
    start_time = time.perf_counter()

    try:
        capacity = int(request.form["capacity"])
    except (ValueError, KeyError):
        return render_template(
            "index.html",
            error="Kapasitas harus berupa angka."
        )

    if capacity <= 0:
        return render_template(
            "index.html",
            error="Kapasitas harus lebih dari 0."
        )

    items = []

    # Maksimal 8 barang
    for i in range(8):
        nama = request.form.get(f"nama{i}", "").strip()
        berat = request.form.get(f"berat{i}", "").strip()
        profit = request.form.get(f"profit{i}", "").strip()

        # Baris kosong diabaikan
        if nama == "" and berat == "" and profit == "":
            continue

        # Jika ada yang belum lengkap
        if nama == "" or berat == "" or profit == "":
            return render_template(
                "index.html",
                error=f"Data barang ke-{i+1} belum lengkap."
            )

        try:
            berat = int(berat)
            profit = int(profit)
        except ValueError:
            return render_template(
                "index.html",
                error=f"Berat dan profit barang ke-{i+1} harus berupa angka."
            )

        if berat <= 0:
            return render_template(
                "index.html",
                error=f"Berat '{nama}' harus lebih dari 0."
            )

        if profit < 0:
            return render_template(
                "index.html",
                error=f"Profit '{nama}' tidak boleh negatif."
            )

        items.append({
            "nama": nama,
            "berat": berat,
            "profit": profit
        })

    # Minimal harus ada 1 barang
    if len(items) == 0:
        return render_template(
            "index.html",
            error="Minimal isi 1 barang."
        )

    # Backup untuk tabel input
    items_input_backup = copy.deepcopy(items)

    # Jalankan DFS + Branch and Bound
    result = solve_knapsack(items, capacity)

    end_time = time.perf_counter()
    execution_time = round(end_time - start_time, 6)

    # PERBAIKAN: Indentasi return statement disesuaikan agar masuk di dalam fungsi solve()
    return render_template(
        "result.html",
        selected_items=result["selected_items"],
        best_profit=result["best_profit"],
        total_weight=result["total_weight"],
        node_count=result["node_count"],
        explored_nodes=result["explored_nodes"],
        execution_time=execution_time,
        capacity=capacity,
        items_input=items_input_backup
    )

# PERBAIKAN SINTAKSIS: Menggunakan dunder (double underscore) yang benar tanpa format bold markdown
if __name__ == "__main__":
    app.run(debug=True)
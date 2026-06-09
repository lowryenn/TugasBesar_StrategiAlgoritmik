def solve_knapsack(items, capacity):
    # Simpan indeks asli (0-7) dari form input ke dalam tiap item sebelum di-sort
    for i, item in enumerate(items):
        item['original_id'] = i

    # 1. SORTING berdasarkan rasio profit/berat secara descending
    items_sorted = sorted(
        items, 
        key=lambda x: x["profit"] / x["berat"] if x["berat"] > 0 else 0, 
        reverse=True
    )

    best_profit = 0
    best_items = []
    node_count = 0
    explored_nodes = []

    # Fungsi pembantu menghitung Upper Bound menggunakan Fractional Knapsack
    def get_bound(index, current_weight, current_profit):
        if current_weight >= capacity:
            return 0
        
        profit_bound = current_profit
        total_weight = current_weight
        j = index
        
        while j < len(items_sorted) and total_weight + items_sorted[j]["berat"] <= capacity:
            total_weight += items_sorted[j]["berat"]
            profit_bound += items_sorted[j]["profit"]
            j += 1
            
        if j < len(items_sorted):
            profit_bound += (capacity - total_weight) * (items_sorted[j]["profit"] / items_sorted[j]["berat"])
            
        return profit_bound

    def dfs(index, current_weight, current_profit, selected_items):
        nonlocal best_profit, best_items, node_count

        # Menghitung node yang sah
        node_count += 1
        explored_nodes.append({
            "level": index,
            "weight": current_weight,
            "profit": current_profit,
            "selected": [item["nama"] for item in selected_items]
        })

        # Base case: semua barang sudah diputuskan
        if index == len(items_sorted):
            if current_profit > best_profit:
                best_profit = current_profit
                best_items = selected_items[:]
            return

        # =====================
        # BRANCH AND BOUND (PRUNING)
        # =====================
        bound = get_bound(index, current_weight, current_profit)
        if bound <= best_profit:
            return  # Cabang tidak menjanjikan dipotong di sini

        # =====================
        # CABANG 1: AMBIL BARANG
        # =====================
        if current_weight + items_sorted[index]["berat"] <= capacity:
            selected_items.append(items_sorted[index])
            dfs(
                index + 1,
                current_weight + items_sorted[index]["berat"],
                current_profit + items_sorted[index]["profit"],
                selected_items
            )
            selected_items.pop()  # Backtracking

        # =====================
        # CABANG 2: TIDAK AMBIL BARANG
        # =====================
        dfs(
            index + 1,
            current_weight,
            current_profit,
            selected_items
        )

    # Jalankan DFS dari root
    dfs(0, 0, 0, [])

    # Sortir kembali barang yang terpilih berdasarkan urutan aslinya di form (1-8)
    best_items.sort(key=lambda x: x['original_id'])

    total_weight = sum(item["berat"] for item in best_items)

    return {
        "best_profit": best_profit,
        "selected_items": best_items,
        "total_weight": total_weight,
        "node_count": node_count,
        "explored_nodes": explored_nodes
    }
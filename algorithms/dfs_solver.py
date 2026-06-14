def solve_knapsack(items, capacity):
    # Simpan urutan asli dari form input
    for i, item in enumerate(items):
        item["original_id"] = i

    # Sorting berdasarkan rasio profit/berat (descending)
    items_sorted = sorted(
        items,
        key=lambda x: x["profit"] / x["berat"],
        reverse=True
    )

    best_profit = 0
    best_items = []
    node_count = 0
    explored_nodes = []

    # Upper Bound menggunakan Fractional Knapsack
    def get_bound(index, current_weight, current_profit):

        # Jika sudah melebihi kapasitas
        if current_weight > capacity:
            return 0

        # Jika kapasitas sudah penuh
        if current_weight == capacity:
            return current_profit

        profit_bound = current_profit
        total_weight = current_weight
        j = index

        # Tambahkan item utuh selama masih muat
        while (
            j < len(items_sorted)
            and total_weight + items_sorted[j]["berat"] <= capacity
        ):
            total_weight += items_sorted[j]["berat"]
            profit_bound += items_sorted[j]["profit"]
            j += 1

        # Tambahkan fractional item
        if j < len(items_sorted):
            remaining = capacity - total_weight

            profit_bound += (
                remaining
                * (
                    items_sorted[j]["profit"]
                    / items_sorted[j]["berat"]
                )
            )

        return profit_bound

    def dfs(index, current_weight, current_profit, selected_items):
        nonlocal best_profit, best_items, node_count

        node_count += 1

        explored_nodes.append({
            "level": index,
            "weight": current_weight,
            "profit": current_profit,
            "selected": [
                item["nama"]
                for item in selected_items
            ]
        })

        # Update solusi terbaik setiap kali profit lebih besar
        if current_profit > best_profit:
            best_profit = current_profit
            best_items = selected_items.copy()

        # Semua item sudah diproses
        if index >= len(items_sorted):
            return

        # Branch and Bound
        bound = get_bound(
            index,
            current_weight,
            current_profit
        )

        if bound <= best_profit:
            return

        item = items_sorted[index]

        # CABANG 1 : Ambil item
        if current_weight + item["berat"] <= capacity:

            selected_items.append(item)

            dfs(
                index + 1,
                current_weight + item["berat"],
                current_profit + item["profit"],
                selected_items
            )

            selected_items.pop()

        # CABANG 2 : Tidak ambil item
        dfs(
            index + 1,
            current_weight,
            current_profit,
            selected_items
        )

    # Mulai DFS
    dfs(0, 0, 0, [])

    # Kembalikan urutan sesuai input awal
    best_items.sort(
        key=lambda x: x["original_id"]
    )

    total_weight = sum(
        item["berat"]
        for item in best_items
    )

    return {
        "best_profit": best_profit,
        "selected_items": best_items,
        "total_weight": total_weight,
        "node_count": node_count,
        "explored_nodes": explored_nodes
    }
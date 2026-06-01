best_profit = 0
best_solution = []
node_count = 0


def reset():
    global best_profit
    global best_solution
    global node_count

    best_profit = 0
    best_solution = []
    node_count = 0


def upper_bound(
        index,
        current_profit,
        profit):

    return current_profit + sum(profit[index:])


def dfs(
        index,
        n,
        berat,
        profit,
        kapasitas,
        current_weight,
        current_profit,
        selected,
        nama):

    global best_profit
    global best_solution
    global node_count

    node_count += 1

    print(
        f"Node {node_count}"
        f" | Level={index}"
        f" | Berat={current_weight}"
        f" | Profit={current_profit}"
        f" | Pilihan={selected}"
    )

    if current_weight > kapasitas:
        return

    if index == n:

        if current_profit > best_profit:

            best_profit = current_profit
            best_solution = selected[:]

        return

    bound = upper_bound(
        index,
        current_profit,
        profit
    )

    if bound <= best_profit:
        return

    selected.append(index)

    dfs(
        index + 1,
        n,
        berat,
        profit,
        kapasitas,
        current_weight + berat[index],
        current_profit + profit[index],
        selected,
        nama
    )

    selected.pop()

    dfs(
        index + 1,
        n,
        berat,
        profit,
        kapasitas,
        current_weight,
        current_profit,
        selected,
        nama
    )


def hasil():
    return best_profit, best_solution, node_count
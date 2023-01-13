def tower_builder(n_floors):
    arr = []
    for i in range(n_floors):
        arr.append(f"{(n_floors - i - 1) * ' '}{(i * 2 + 1) * '*'}{(n_floors - i - 1) * ' '}")
    return arr

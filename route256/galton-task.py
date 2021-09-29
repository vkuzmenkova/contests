def get_all_sum(arr: list):
    final = []
    for row in arr:  # высота рулетки
        print(row)


if __name__ == "__main__":
    x = int(input())  # кол-во рулеток
    roulettes = []
    for i in range(x):
        h = int(input())  # Высота рулетка
        roulette = []
        for j in range(h):
            roulette.append(list(map(int, input().split())))
        roulettes.append(roulette)

    print(get_all_sum(roulettes[0]))

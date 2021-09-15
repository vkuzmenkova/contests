def min_operations(input_list) -> int:
    if input_list == sorted(input_list):
        return max(input_list) - min(input_list)

    return -1


n = int(input())
reservoirs = list(map(int, input().split()))

print(min_operations(reservoirs))
if __name__ == "__main__":
    input_arr = list(map(int, input().split()))
    n = input_arr[0]
    L = input_arr[1]

    if L % n == 0:
        print(L // n)
    else:
        print(L // n + 1)

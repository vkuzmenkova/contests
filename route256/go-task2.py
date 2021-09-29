def get_num_apples(arr: list):
    arr.sort()
    sum = 0
    for i in range(0, len(arr), 2):
        sum += arr[i + 1] - arr[i]

    return sum


if __name__ == "__main__":
    n = int(input())  # всегда четное
    a = list(map(int, input().split()))
    print(get_num_apples(a))

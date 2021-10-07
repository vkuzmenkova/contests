if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    n = input_list[1]

    numbers = list(map(int, input().split()))

    for i in range(n - 1):
        if len(numbers) > 0:
            max_n = max(numbers)
            for j in range(numbers.count(max_n)):
                numbers.remove(max_n)
        # numbers = list(filter(lambda x: x != max(numbers), numbers))
        else:
            break

    print(max(numbers)) if len(numbers) > 0 else print(-1)

def is_possible_to_get_num(x: int):
    if (x % 100) % 11 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    t = int(input())
    input_arr = [int(input()) for i in range(t)]
    for i in input_arr:
        if is_possible_to_get_num(i):
            print('YES')
        else:
            print('NO')

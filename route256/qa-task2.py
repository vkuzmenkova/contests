import json


def to_excel_format(number: int) -> str:
    start = ord('A') - 1
    integer = number // 26
    remainder = number % 26

    if remainder == 0:
        remainder = 26
        integer = integer - 1

    if number <= 26:
        return chr(start + remainder)
    else:
        return chr(start + integer) + chr(start + remainder)


if __name__ == "__main__":
    input_str = input()
    number = int(input_str)

    answer = to_excel_format(number)

    print(json.dumps(answer))

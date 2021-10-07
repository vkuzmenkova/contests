# Повернуть матрицу (опрокинуть на правый бок)
import json


def rotate_matrix(matrix):
    return list(map(list, list(zip(*matrix[::-1]))))


if __name__ == "__main__":
    input_str = input()
    matrix = json.loads(input_str)

    answer = rotate_matrix(matrix)

    print(json.dumps(answer))

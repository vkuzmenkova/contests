# Найти комбинации элементов переданных массивов
import json


def get_combinations(list1, list2):
    result = []

    for j in list1:
        for k in list2:
            tmp = [j, k]
            result.append(tmp)

    return result


def get_flat_list(input_list, depth=-1):
    result = []
    for element in input_list:
        if depth == 0 or type(element) is not list:
            result.append(element)
        else:
            result.extend(get_flat_list(element, depth - 1))
    return result


def pairwise(*lists):
    zero_lists = list(filter(lambda x: len(x) == 0, lists))
    if len(zero_lists) > 0:
        return []

    if len(lists) == 1:
        return list(map(lambda x: [x], lists[0]))

    filtered_lists = lists[0]

    for i in range(1, len(lists)):
        if len(lists[i]) > 0:
            filtered_lists = get_combinations(filtered_lists,
                                              lists[i])

    combinations = list(map(get_flat_list, filtered_lists))

    return combinations


if __name__ == "__main__":
    input_str = input()
    lists = json.loads(input_str)
    answer = pairwise(*lists)
    # answer = pairwise([1], [1, [3]])
    # answer = pairwise([1, 2, 3], [9], [['k', 'i'], 'o'])

    print(json.dumps(answer))

import copy


def find_closest_previous(input_list, index):
    input_list.reverse()
    prev = None
    for day in input_list:
        if day[1] is not None:
            prev = day[1]
            break

    return prev


def is_day_in_list(input_list, n: int):
    indexes = [i[0] for i in input_list]
    return True if indexes.count(n) > 0 else False


def fill_gaps(data, first_day: int, last_day: int, today: int):
    # add days
    for i in range(first_day, last_day + 1):
        if not is_day_in_list(data, i):
            data.append([i, None])

    data.sort(key=lambda x: x[0])
    # filled_list = copy.deepcopy(data)
    filled_list = data.copy()

    # fill in values
    for day in filled_list:
        if day[0] > today:
            day[1] = -1
        else:
            if day[1] is None or day[1] == -1:
                prev = find_closest_previous(
                    filled_list[0:filled_list.index(day)],
                    day[0])
                if prev is None:
                    day[1] = -1
                else:
                    day[1] = prev

    return filled_list


if __name__ == "__main__":

    # input
    first_day, last_day, today, num = list(map(int, input().split()))
    data = []

    for i in range(num):
        day_data = list(map(int, input().split()))
        data.append(day_data)

    chart_data = fill_gaps(data, first_day, last_day, today)

    for day in chart_data:
        if first_day <= day[0] <= last_day:
            print(f"{day[0]} {day[1]}")

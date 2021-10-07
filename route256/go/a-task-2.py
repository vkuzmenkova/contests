def get_prev_value(data_day, data_value, day):
    if day < data_day[-1]:
        return -1
    if day > data_day[0]:
        return data_value[0]

    prev = -100
    for day_temp in range(data_day[-1], data_day[0]):
        if day != day_temp:
            if data_day.count(day_temp) > 0:
                index_value = data_day.index(day_temp)
                prev = data_value[index_value]
        else:
            return prev


if __name__ == "__main__":

    # input
    first_day, last_day, today, num = list(map(int, input().split()))
    data = []
    data_day = []
    data_value = []

    for i in range(num):
        input_data = list(map(int, input().split()))
        data_day.append(input_data[0])
        data_value.append(input_data[1])

    chart_data = []

    for day in range(first_day, last_day + 1):
        if day > today:
            print(day, -1)
        else:
            if data_day.count(day) > 0:  # если данные есть в БД
                index_value = data_day.index(day)
                if data_value[index_value] != -1:
                    print(day, data_value[index_value])
                else:
                    print(day, get_prev_value(data_day, data_value, day))
            else:
                print(day, get_prev_value(data_day, data_value, day))

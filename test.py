def find_sum(num):
    if isinstance(num, int) is True:
        summ = 0
        while num // 10 != 0:
            summ += num % 10
            num = num // 10
        return summ + num
    else:
        return "Че, самый умный?"


def sum_long_number():
    assert find_sum(34212341) == 20


def sum_zero():
    assert find_sum(0) == 0


def sum_string():
    assert find_sum("") == "Че, самый умный?"


sum_long_number()
sum_zero()
sum_string()


def max_value(num):
    # return int("9" * num)
    # sum = 0
    # pow_of_ten = 0
    # for i in range(num):
    #     sum += 9 * (10 ** pow_of_ten)
    #     pow_of_ten += 1
    # return sum
    return 10 ** num - 1


print(max_value(1))

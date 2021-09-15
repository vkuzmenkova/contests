def parse_symbol(symbol):
    if symbol == '.':
        return False
    if symbol == '#':
        return True


def parse_line(input_arr):
    return [
        parse_symbol(input_arr[0]),
        parse_symbol(input_arr[1]),
        parse_symbol(input_arr[2]),
        parse_symbol(input_arr[4]),
        parse_symbol(input_arr[5]),
        parse_symbol(input_arr[6])
    ]


def find_seats(num, side, position, available_seats_plan):
    desirable_seat = None
    is_seats_available = False
    if side == "left" and position == "window":
        desirable_seat = 0
        for row in available_seats_plan:
            for i in num:
                if row[i] == False:
                    is_seats_available = True
                    
    if side == "left" and position == "aisle":
        desirable_seat = 2
    if side == "rigth" and position == "window":
        desirable_seat = 5
    if side == "rigth" and position == "aisle":
        desirable_seat = 3







n = int(input())
seats_availability = []

for i in range(n):
    seats_availability[i] = parse_line(input.split())

m = int(input())
seats_needs = []

for i in range(m):
    seats_needs.append(input().split())

# 2 left aisle

for i in seats_needs:
    pass

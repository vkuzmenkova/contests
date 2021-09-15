a, b, c = int(input()), int(input()), int(input())

if a == 0:
    print("MANY SOLUTIONS")
solution = (c ** 2 - b) / a
if c < 0 or -b / a < 0 or type(solution) is not int:
    print("NO SOLUTION")
else:
    solution = (c ** 2 - b) / a
    print(int(solution))



def compare_sides(side_1, side_2, compare_to_side):
    return True if side_1+side_2 > compare_to_side else False

def main():
    a, b, c = int(input()), int(input()), int(input())
    print("YES" if compare_sides(a, b, c) and
          compare_sides(a, c, b) and
          compare_sides(b, c, a)
          else "NO")


if __name__ == "__main__":
    main()

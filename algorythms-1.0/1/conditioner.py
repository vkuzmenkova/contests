def is_tcond_lower(troom, tcond):
    return True if tcond < troom else False


def main():
    input_list = list(map(int, input().split()))
    troom, tcond = input_list[0], input_list[1]
    mode = input()

    CONDITIONER_MODE = {
        "freeze": tcond if is_tcond_lower(troom, tcond) else troom,
        "heat": troom if is_tcond_lower(troom, tcond) else tcond,
        "auto": tcond,
        "fan": troom,
    }

    print(CONDITIONER_MODE[mode])


if __name__ == "__main__":
    main()

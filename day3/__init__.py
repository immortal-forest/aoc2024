from utils import load_data


def part1():
    data = load_data("day3/input", False)
    total = 0
    while True:
        s = data.find("mul(")
        if s == -1:
            break
        sub = ""
        valid = False
        for d, i in enumerate(data[s + 4 :], start=s + 4):
            if i.isspace() or i.isalpha() or i in "~`!@#$%^&*_-./-+=<>?|\\[]{}":
                valid = False
                break
                # invalid mul found break or continue
            elif i.isdigit():
                sub += i
                valid = True
            elif i == ",":
                if "," in sub:
                    valid = False
                    break
                sub += i
                valid = True
            elif i == ")":
                valid = True
                break
        if valid:
            lst = sub.split(",")
            if len(lst) == 2:
                nums = list(map(int, lst))
                total += nums[0] * nums[1]
        data = data[d + 1 :]
    print(f"Sum: {total}")


def part2():
    data = load_data("day3/input", False)
    total = 0
    old_s = 0
    do = True
    while True:
        s = data.find("mul(")
        if s == -1:
            break
        sub = ""
        valid = False
        for d, i in enumerate(data[s + 4 :], start=s + 4):
            if i.isspace() or i.isalpha() or i in "~`!@#$%^&*_-./-+=<>?|\\[]{}":
                valid = False
                break
                # invalid mul found break or continue
            elif i.isdigit():
                sub += i
                valid = True
            elif i == ",":
                if "," in sub:
                    valid = False
                    break
                sub += i
                valid = True
            elif i == ")":
                valid = True
                break

        # do and don'ts
        for i in range(len(data[:d])):
            part = data[i:d]
            if part.find("do()") > -1:
                do = True
                continue
            if part.find("don't()") > -1:
                do = False
                continue

        if valid:
            lst = sub.split(",")
            if len(lst) == 2:
                if do:
                    nums = list(map(int, lst))
                    total += nums[0] * nums[1]

        data = data[d + 1 :]
    print(f"Sum: {total}")

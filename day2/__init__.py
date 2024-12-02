from utils import load_data


def check_safe(lvls: list):
    line_safe = False
    state = -2
    for idx, nums in enumerate(lvls):
        nums = int(nums.strip())
        try:
            adj_num = int(lvls[idx + 1].strip())
        except IndexError:
            break
        if adj_num > nums:
            # increasing
            if state == 1 or state == -1:
                line_safe = False
                break
            count = adj_num - nums
            state = 0
        elif nums > adj_num:
            # decreasing
            if state == 0 or state == -1:
                line_safe = False
                break
            count = nums - adj_num
            state = 1
        else:
            # adj nums are same
            state = -1
            line_safe = False
            break

        if count <= 3 and count > 0:
            line_safe = True
        else:
            line_safe = False
            break
    return line_safe, idx


def part1():
    data = load_data("day2/input")
    safe = 0
    for line in data:
        lvls = line.split(" ")
        line_safe, _ = check_safe(lvls)
        if line_safe:
            safe += 1

    print(f"Safe reports: {safe}")


def part2():
    data = load_data("day2/input")
    safe = 0
    for line in data:
        lvls = line.split(" ")
        line_safe, idx = check_safe(lvls)
        if line_safe:
            safe += 1
        else:
            # bruteforcing....
            safeness = []
            count = 0
            while count < len(lvls):
                new_lvls = lvls.copy()
                new_lvls.pop(count)
                line_safe, idx = check_safe(new_lvls)
                safeness.append(line_safe)
                count += 1

            # check if we have at least one case where the line is safe
            if True in safeness:
                safe += 1

    print(f"Safe reports: {safe}")

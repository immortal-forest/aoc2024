from utils import load_data


def part1():
    left_list = []
    right_list = []
    data = load_data("day1/input")
    for line in data:
        l, *_, r = line.split(" ")
        left_list.append(int(l.strip()))
        right_list.append(int(r.strip()))

    total_distance = []
    # getting min elements on each iteration until lists are empty
    while True:
        if not left_list and not right_list:
            break
        min_left, min_right = min(left_list), min(right_list)
        distance = abs(min_left - min_right)
        total_distance.append(distance)
        left_list.remove(min_left)
        right_list.remove(min_right)
    print(f"Total distance: {sum(total_distance)}")


def part2():
    left_list = []
    right_list = []
    data = load_data("day1/input")
    for line in data:
        l, *_, r = line.split(" ")
        left_list.append(int(l.strip()))
        right_list.append(int(r.strip()))

    similarity_score = []
    left_count = len(left_list)
    for i in range(left_count):
        item = left_list[i]
        occurs = right_list.count(item)
        sim_score = item * occurs
        similarity_score.append(sim_score)
    print(f"Total similarity score: {sum(similarity_score)}")

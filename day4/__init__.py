from utils import load_data


def part1():
    data = [l.strip() for l in load_data("day4/input")]
    total_xmas = 0
    for row in range(len(data)):
        line = data[row]
        # counting horizontally
        h_count = line.count("XMAS")
        rev_h_count = line[::-1].count("XMAS")
        total_xmas += h_count + rev_h_count

        for col in range(len(line)):
            char = line[col]
            if char == "X":
                # counting vertically
                # checking above
                check_str_above = ""
                if row >= 3:
                    for i in range(row - 1, row - 4, -1):
                        check_str_above += data[i][col]
                    if char + check_str_above == "XMAS":
                        total_xmas += 1

                # checking below
                check_str_below = ""
                if row + 3 < len(data):
                    for j in range(row + 1, row + 4):
                        check_str_below += data[j][col]
                    if char + check_str_below == "XMAS":
                        total_xmas += 1

                # counting diagnoally
                # top-left
                d_tl = ""
                if row >= 3 and col >= 3:
                    d_tl_col = col - 1
                    for i in range(row - 1, row - 4, -1):
                        d_tl += data[i][d_tl_col]
                        d_tl_col -= 1
                    if char + d_tl == "XMAS":
                        total_xmas += 1

                # top-right
                d_tr = ""
                if row >= 3 and col + 3 < len(line):
                    d_tr_col = col + 1
                    for j in range(row - 1, row - 4, -1):
                        d_tr += data[j][d_tr_col]
                        d_tr_col += 1
                    if char + d_tr == "XMAS":
                        total_xmas += 1

                # bottom-left
                d_bl = ""
                if row + 3 < len(data) and col >= 3:
                    d_bl_col = col - 1
                    for x in range(row + 1, row + 4):
                        d_bl += data[x][d_bl_col]
                        d_bl_col -= 1
                    if char + d_bl == "XMAS":
                        total_xmas += 1

                # bottom-right
                d_br = ""
                if row + 3 < len(data) and col + 3 < len(line):
                    d_br_col = col + 1
                    for y in range(row + 1, row + 4):
                        d_br += data[y][d_br_col]
                        d_br_col += 1
                    if char + d_br == "XMAS":
                        total_xmas += 1

    print(f"Total XMASes: {total_xmas}")


def part2():
    data = [l.strip() for l in load_data("day4/input")]
    total_x_mas = 0
    for row in range(len(data)):
        line = data[row]
        for col in range(len(line)):
            char = line[col]

            if row >= 1 and row + 1 < len(line) and col >= 1 and col + 1 < len(line):
                if char == "A":
                    tl = data[row - 1][col - 1]
                    tr = data[row - 1][col + 1]
                    bl = data[row + 1][col - 1]
                    br = data[row + 1][col + 1]
                    s1 = set(char + tl + br)
                    s2 = set(char + bl + tr)
                    if s1 == s2 == {"M", "S", "A"}:
                        total_x_mas += 1

    print(f"Total X-MASes: {total_x_mas}")


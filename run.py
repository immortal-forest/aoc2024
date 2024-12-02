import importlib
import os
import sys
from time import time


def main(args: list):
    if not args:
        print("Day required!")
        return

    if args[0] == "help":
        print("run.py day [part]")
        return

    if args[0] == "gen":
        try:
            day = int(args[1])
            if day > 25 or day < 1:
                raise ValueError
        except IndexError:
            print("Day required to generate files")
            return
        except ValueError:
            print("Day must be from 1-25")
            return

        try:
            os.mkdir(f"day{day}")
            with open(f"day{day}/__init__.py", "w") as file:
                file.write("def part1():\n\tpass\n\n\ndef part2():\n\tpass")
            print(f"Files generated for day-{day}")
            return
        except FileExistsError:
            print(f"Files for day-{day} already exists!")
            return

    day = args[0]
    if int(day) < 1:
        print("Invalid day!")
        return

    try:
        part = int(args[1])
    except ValueError:
        print("Part can only be 1, 2 or 0")
        return
    except IndexError:
        part = 0

    print("\n" + "=" * 50)
    print(f"\nRunning day-{day} solution\n")
    module = importlib.import_module(f"day{day}")
    match part:
        case 0:
            print("Part 1:", end="\n\t")
            s1 = time()
            module.part1()
            e1 = time()
            print(f"\tTook: {e1-s1}")
            print("Part 2:", end="\n\t")
            s2 = time()
            module.part2()
            e2 = time()
            print(f"\tTook: {e2-s2}")

        case 1:
            print("Part 1:", end="\n\t")
            s1 = time()
            module.part1()
            e1 = time()
            print(f"\tTook: {e1-s1}")

        case 2:
            print("Part 2:", end="\n\t")
            s2 = time()
            module.part2()
            e2 = time()
            print(f"\tTook: {e2-s2}")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main(sys.argv[1:])

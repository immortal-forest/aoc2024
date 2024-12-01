import importlib
import sys


def main(args: list):
    if not args:
        print("Day required!")
        return

    if args[0] == "help":
        print("run.py day [part]")
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
            module.part1()
            print("Part 2:", end="\n\t")
            module.part2()

        case 1:
            print("Part 1:", end="\n\t")
            module.part1()

        case 2:
            print("Part 2:", end="\n\t")
            module.part2()
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main(sys.argv[1:])

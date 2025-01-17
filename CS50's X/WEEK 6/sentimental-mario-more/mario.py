from cs50 import get_int


def main():

    height = get_height()

    for i in range(height):
        print_row(height - i - 1, i + 1)


def get_height():

    while True:
        height = get_int("Height: ")
        if height > 0 and height < 9:
            return height


def print_row(spaces, briks):

    for i in range(spaces):
        print(" ", end="")

    for i in range(briks):
        print("#", end="")

    print("  ", end="")

    for i in range(briks):
        print("#", end="")

    print()


main()

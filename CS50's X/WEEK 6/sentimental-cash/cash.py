from cs50 import get_float


def main():

    coins = 0

    while True:
        change = get_float("Change owed: ")
        if change > 0:
            change = 100 * change
            break

    while (change >= 25):
        coins += 1
        change -= 25

    while (change >= 10):
        coins += 1
        change -= 10

    while (change >= 5):
        coins += 1
        change -= 5

    while (change >= 1):
        coins += 1
        change -= 1

    print(f"{coins}")


main()

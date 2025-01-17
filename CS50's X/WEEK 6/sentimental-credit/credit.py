from cs50 import get_int, get_string


def main():

    card = get_int("Number: ")

    sum = 0

    # adding the numbers that are not multiplied by 2 and counting them.

    card_aux = card  # creating a temp variable to not lose "card" value.

    while card_aux > 0:
        sum += card_aux % 10
        card_aux //= 100

    # adding the numbers that are multiplied by 2 and counting them

    card_aux = card // 10  # updanting the temp variable

    while card_aux > 0:
        remainder = card_aux % 10

        if remainder < 5:
            sum += 2 * remainder
        else:
            sum += 2 * remainder - 9

        card_aux //= 100

    # verifying the card

    sum = sum % 10

    if sum == 0:

        length = 1  # counting the card length
        digits = 0  # aux variable to store the first 2 digits
        card_aux = card  # updanting the temp variable

        while card_aux >= 10:
            digits = card_aux
            length += 1
            card_aux //= 10

        if ((length == 13 or length == 16) and digits // 10 == 4):
            print("VISA")

        elif ((length == 15 and digits == 34) or digits == 37):
            print("AMEX")

        elif (length == 16 and digits > 50 and digits < 56):
            print("MASTERCARD")

        else:
            print("INVALID")

    else:
        print("INVALID")


main()

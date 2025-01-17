def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s.isalnum():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] != "0" and s[i:].isdigit():
                return True
            else:
                return False

main()

from cs50 import get_string


def main():
    text = get_string("Text: ")

    words = 1
    letters = 0
    sentences = 0

    for c in text:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            words += 1
        elif c in ['?', '!', '.']:
            sentences += 1

    index = round(0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


main()

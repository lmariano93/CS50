import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s):
        return f"https://youtu.be/{match.group(2)}"
    return None


if __name__ == "__main__":
    main()

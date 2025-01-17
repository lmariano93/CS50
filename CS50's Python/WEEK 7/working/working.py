import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)


def convert(s):
    match = re.match(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)
    if not match:
        raise ValueError

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
    start_24 = format_24(start_hour, start_minute, start_period)
    end_24 = format_24(end_hour, end_minute, end_period)
    return f"{start_24} to {end_24}"


def format_24(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0
    if not (1 <= hour <= 12) or not (0 <= minute < 60):
        raise ValueError
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()

from datetime import date, datetime
import inflect
import sys

def main():
    birthday = input("Date of birth: ")
    difference_minutes = calculate_minutes(birthday)
    if difference_minutes:
        print(format_minutes(difference_minutes))

def calculate_minutes(birthday):
    try:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
        difference_minutes = (date.today() - birth_date).days * 24 * 60
        return difference_minutes
    except ValueError:
        sys.exit("Invalid date")

def format_minutes(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()

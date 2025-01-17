def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_input = input("Date: ")
        try:
            if '/' in date_input:
                month, day, year = date_input.split('/')
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

            elif ',' in date_input:
                month, rest = date_input.split(' ', 1)
                day, year = rest.split(',')
                day = int(day)
                year = int(year)

                if month in months and 1 <= day <= 31:
                    month_number = months.index(month) + 1
                    print(f"{year:04d}-{month_number:02d}-{day:02d}")
                    break

        except ValueError:
            pass

main()

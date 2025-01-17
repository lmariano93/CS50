def main():
    time = input("What time is it? ").strip()

    time_in_hours = convert(time)

    if 7.0 <= time_in_hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("Dinner time")

def convert(time):
    time_split = time.split(':')
    hours = int(time_split[0])
    minutes = int(time_split[1])
    return hours + minutes / 60

if __name__ == "__main__":
    main()

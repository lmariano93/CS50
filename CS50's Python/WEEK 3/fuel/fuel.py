def main():
    x = get_int()
    print(f"{x}")


def get_int():
    while True:
        try:
            x = input("Fraction: ")
            a, b = map(int, x.split('/'))
            c = (a/b)*100
            if a <= b:
                if c >= 99:
                    return "F"
                elif c <= 1:
                    return "E"
                else:
                    return(f"{round(float(c))}%")
            pass
        except (ValueError, ZeroDivisionError):
            pass


main ()

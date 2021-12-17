def leap_year_one_line(year):
    print("Leap year" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "Not a leap year.")


def leap_year_if_cond(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    print("Leap year" if leap else "Not a leap year")


if __name__ == '__main__':
    year = int(input("Which year do you want to check? "))
    leap_year_one_line(year)
    leap_year_if_cond(year)

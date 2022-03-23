# This proggram calculate date for you if you add or subtract days from the date.
# Without built_in function
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
days = int(input("Enter days: "))
another_days = int(input("Enter another days: "))
if days > 1000:
    quit(print("Enter day smaller than 1000"))
if year < 1900 or year > 2022:
    quit(print("Enter year between 1900 and 2022"))
if month > 12:
    quit(print("Enter month between 1 and 12"))
if another_days > 0:
    total_days = another_days + days
    while total_days > 31 or total_days > 28 or total_days > 30:
        if month in (1, 3, 5, 7, 8, 10, 12):   # 31 days
                total_days = total_days - 31
                month += 1
                days = total_days
        elif month == 2:   # 28 days
                total_days = total_days - 28
                month += 1
                days = total_days
        elif month in (4, 6, 9, 11):    # 30 days
            total_days = total_days - 30
            month += 1
            days = total_days
        else:
            print("Enter month between 1 and 12")
    if month > 12:
        year += 1
        month -= 12
    print(year, ",", month, ",", total_days)
else:
    another_positive_days = -another_days
    total_days = another_positive_days - days
    month -= 1
    while total_days > 28 or month == 0:
        if month in (1, 3, 5, 7, 8, 10, 12):  # 31 days
            total_days = total_days - 31
            month -= 1
        elif month == 2:  # 28 days
            total_days = total_days - 28
            month -= 1
        elif month in (4, 6, 9, 11):  # 30 days
            total_days = total_days - 30
            month -= 1
        if month == 0:
            year -= 1
            month += 12
            if total_days > 28:
                continue
    if month in (1, 3, 5, 7, 8, 10, 12):
        total_days = 31 - total_days
    elif month == 2:
        total_days = 28 - total_days
    else:
        total_days = 30 - total_days

    print(year, ",", month, ",", total_days)
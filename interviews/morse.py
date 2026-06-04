# Leap year last one was 2024
# If the year is %4 100 is not 400 is however

def print_leap_year():
    starting_year = 1582+2
    current_year = 2026

    # if year % 4 - 1582
    years_to_examine = current_year - starting_year
    for year in range(years_to_examine):
        if current_year % 100 == 0:
            if current_year%400 == 0:
                print(year+starting_year)
            continue
        if year%4 == 0:
            print(year+starting_year)

print_leap_year()


year = int(input('enter a year: '))
if (year % 4 == 0 and year / 100 != 0) or (year / 400 == 0):
    print(f'the year of {year} is a leap year')
else:
    print(f'the year of {year} is not a leap year')

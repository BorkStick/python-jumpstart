from datetime import date


def title(text):
    print("------------------")
    print(text)
    print("------------------")
    print()

title('BIRTHDAY APP')

birth_year = 0
birth_month = 0
birth_day = 0 

# ask user for year born
birth_year = input("What YEAR were you born [YYYY]? ")

# ask user for month 
birth_month = input("What MONTH were you born [MM]? ")

# ask user for day 
birth_day = input("What DAY were you born [DD]? ")

# print out full birthday with month day and year
print(f'You were born {birth_month}/{birth_day}/{birth_year}')

days_left = 0
current_date = date.today()
print(current_date.year)


print(f'It looks like your birthday is in {days_left} days.')


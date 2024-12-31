# Function to judge if it is leap year or normal year

def year(number):
    if number % 4 != 0:
        return 'Normal Year'
    elif number % 4 == 0 and number % 100 != 0:
        return 'Leap Year'
    elif number % 100 == 0 and number % 400 != 0:
        return 'Normal Year'
    elif number % 400 == 0 and number % 3200 != 0:
        return 'Leap Year'

print('Hi! This function can judge year is leap year or normal year')
year_user_input = int(input('Please input year number (e.g. 2000, 1878...): '))
result = year(year_user_input)

print(year_user_input, 'is your input year and it is', result)
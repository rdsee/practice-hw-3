try:
    week_day = int(input('Enter the number of the week day: '))

    match week_day:
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
        case _:
            print('Invalid input')
except ValueError as e:
    print(f'Error {e}')


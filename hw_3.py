while True:
    try:
        try:
            num1 = int(input('Enter first number: '))
        except ValueError:
            print('Please enter a number')
            print('\t')
            continue
        try:
            num2 = int(input('Enter second number: '))
        except ValueError:
            print('Please enter a number')
            print('\t')
            continue

        math_action = input('Enter a math action: ')

        match math_action:
            case '+' :
                print(f'{num1} + {num2} = {num1 + num2}' )
                print('\t')
            case '-' :
                print(f'{num1} - {num2} = {num1 - num2}' )
                print('\t')
            case '*' :
                print(f'{num1} * {num2} = {num1 * num2}' )
                print('\t')
            case '/' :
                match num2:
                    case 0:
                        raise ZeroDivisionError('You cannot divide by zero')
                print(f'{num1} / {num2} = {num1 / num2}' )
                print('\t')

            case _:
                raise Exception('Not allowed action')
    except Exception as er2:
        print(f'Error: {er2}')
        print('\t')
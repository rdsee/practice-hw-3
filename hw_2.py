try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    match 'x':
        case _ if num1 == num2:
            print('Numbers are equal')
        case _ if num1 > num2:
            print(num1, num2)
        case _ if num1 < num2:
            print(num2, num1)
except ValueError:
    print('Please enter a number')



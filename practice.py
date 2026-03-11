
print ('1. first \n2. second \n3. third \n4. fourth')
user_select = int(input("enter your choice: "))

match user_select:
    case 1:
        print ('1')
    case 2:
        print ('2')
    case 3:
        print("3")
    case 4:
        print ('4')
    case _:
        print('error')

print('\t')

try:
    num1 = int(input(print('Enter the first number: ')))
    num2 = int(input(print('Enter the second number: ')))

    result = num1 / num2
    print(f'result: {result}')

except ZeroDivisionError as error_1:
    print('You cannot divide by zero')
    print(f'Error: {error_1}')
except ValueError as error_2:
    print('You need to enter a number')
    print(f'Error: {error_2}')
except Exception as error_3:
    print('Exception occured!')
    print(f'Error: {error_3}')
finally:
    print('End of calculation')


try:
    print ('1. first \n2. second \n3. third \n4. fourth')
    user_select = int(input("enter your choice: "))

    match user_select:
        case 1:
            print('1')
        case 2:
            print('2')
        case 3:
            print("3")
        case 4:
            print('4')
        case _:
            print('error')
except ValueError as err1:
    print('You need to enter a number')
    print(f'Error: {err1}')
finally:
    print('End of entering your choice')

print('\t')

try:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

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
    print('\t')


try:
    user_age = int(input('Enter your age: '))

    if user_age < 0:
        raise Exception('Age cannot be negative')
    if user_age < 21:
        print('Your age is less than 21, so you cannot buy an alcohol')
    else:
        print('Cash or Card?')
except Exception as error_4:
    print(f'Error: {error_4}')
print('\t')

i = 1
while i < 10:
    print(i, end =" ")
    i += 1


i = 0
while True:

    i += 2

    if i == 10:
        print('countinue...')
        continue
    if i == 20:
        print('break')
        break
    print(i)








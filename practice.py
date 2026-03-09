print("hell oowdld")

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


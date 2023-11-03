print("This is calculator \n")

operation = input("Enter end to finish programm or press enter to continue. ")



while operation != 'end':
    num1 = input("First number is ")
    num2 = input("Second number is ")
    operation = input("Enter the operation +, -, *, / or end to finish programm ")

    if operation == '+':
        print("Result of addition is " + str(int(num1) + int(num2)))
    elif operation == '-':
        print("Result of substraction is " + str(int(num1) - int(num2)))
    elif operation == '*':
        print("Result of multiplication is " + str(int(num1) * int(num2)))
    elif operation == '/':
        print("Result of division is " + str(int(num1) / int(num2)))
    else:
        print("NO OPERATION")
print('end')


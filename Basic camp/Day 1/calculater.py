print("This is calculator \n")

operation = input("Enter the operation +, -, *, /.")

num1 = input("First number is ")
num2 = input("Second number is ")

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


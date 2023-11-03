print("Please login")

name = input("Enter your user name ")
password = input("Enter your password ")

checkName = input("To go to the program enter your name ")
checkPassword = input(" and password ")

if name == checkName and password == checkPassword:
    print("You are login successfully!")
elif name == checkName or password == checkPassword:
    print("Your credentials are incorect")
else:
    print("Try again.")

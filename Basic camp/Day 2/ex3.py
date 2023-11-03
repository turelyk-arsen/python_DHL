import random

print('The menu')

bill = input('Enter bill if you want to finish or enter to order the dish. ')
count = 0

while bill != 'bill':
    bill = input('Enter your dish or bill to pay for everything. ')

    if bill != 'bill':
       price = random.randint(0, 100)
       count = count + price
       print("I'll have " + bill + " and the price is " + str(price) + " euro")
    
print('Bye, your bill is ', count)
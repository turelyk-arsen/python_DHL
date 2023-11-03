answer = input("Did you have lunch today?")
counter = 1

while answer != 'yes' and answer != 'no' :
    print('Please answer yes of no')
    counter = counter + 1
    answer = input('Did you have lunch today? ')
print("I asked ", counter, " times")
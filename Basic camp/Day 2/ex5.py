letter = input('enter your letter ')
number = int(input('enter your number '))

alphabet ='abcdefghijklmnopqrstuvwyz'

if len(alphabet) > number:
    print('your letter is ', alphabet[number-1])
else:
    print('your number is incorect')

for x in alphabet:
    if x == letter:
        #print(x)
        res = alphabet.find(x)+1
        print('the number of your letter is ', res)

    

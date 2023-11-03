print('MENU')

ask = True
bill = 0

while ask:
    print('1 dish is pizza and cost 10 euros')
    print('2 dish is pasta and cost 15 euros')
    print('3 dish is cake and cost 5 euros')

    answer = input('type your answer ')

    if answer == '1' or answer == 'pizza':
        print('your order is pizza and cost 10 euros')
        bill +=10
    elif answer == '2' or answer == 'pasta':
        print('your order is pasta and cost 10 euros')
        bill +=15
    elif answer == '3' or answer == 'cake':
        print('your order is pasta and cost 5 euros')
        bill +=5
    elif answer == 'bill':
        print('you order and ')
        ask = False
    else:
        print('Sorry, your answer is wrong')
print ('your bill is ', bill)
    
    
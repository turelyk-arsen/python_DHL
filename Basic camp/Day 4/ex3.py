print("        Hangman game")
print('*********************************')
print('You have to guess the world.')
print('\n\n')

word = input('Enter the world: ')
des = input('Describe your world: ')

result = True

count = len(word) + 5
times = 0
newWord =list("_"*len(word)) 

while result:
    print("The word has lenght ", len(word), " letters and means - ", des)
    print('You can guess ', count-times, ' times.')

    print('\n\n')
    answer = input('Try to guess the whole word. ')

    times += 1
    if count == times:
        result = False
        print('You took all attempts.')


    if word == answer:
        print('You are WINNER!')
        result = False
    else:
        print("Sorry.")

        print('\n\n')
        letter = input('Try to guess the letter is the word: ')

        for x in range(len(word)):      
            if word[x] == letter:
                print('You guess the letter')
                newWord[x] = letter

        userWord =''.join(newWord)
        print("Your word is ", userWord)

        if userWord == word:    
            print('You are WINNER!')
            result = False

print('\n\n')
print('Game is over')



print("Hangman game")
print('You have X attempts to guess the world.')

word = input('Enter the world: ')
des = input('Describe your world: ')
userWord= list()

result = True

count = len(word) + 5
times = 0

while result:
    print("The word has lenght ", len(word), " letters and means - ", des)
    print('You can guess ', count-times, ' times.')

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

    letter = input('Try to guess the letter is the word: ')
    for x in range(len(word)):
        if word[x] == letter:
            print('You guess the letter')
            userWord.insert(x, letter)
            print("Your word has ", userWord)

            
    
           # print('You are WINNER!')
           # result = False


print('Game is over')



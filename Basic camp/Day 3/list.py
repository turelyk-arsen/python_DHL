sentence = 'hello, how is his home'

print("'" + sentence + "'")
newSent = sentence.split('h')
print(newSent)

number = len(newSent)
print(number)

for i in range(number):
    print(i)
    print(newSent[i])

#error
#print(newSent[number])
print(newSent[number-1])

list_name = ['1', '2', '3']
newText = " ".join(list_name)
print(newText)

new_string = "+".join(newText[1, number-1])



example = {"1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "8":"h", "5":"e", "12":"l", "15":"o"}

sentence = input('enter your sentence: ')
num= ''
letter = ''

for let in sentence: 
    for x, y in example.items():
        if let == y:
            num += x+" " 
        if let == x:
            num += y           
print(num)


sentenceNum = input('enter letter number with space: ').split(' ')
for let in sentenceNum: 
    for x, y in example.items():
        if let == x:
            letter += y           
print(letter)

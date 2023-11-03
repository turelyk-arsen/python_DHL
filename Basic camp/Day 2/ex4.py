print('memorizing multiplication tables ')
number = int(input('ENTER NUMBER '))

for x in range(20):
    result = (x+1) *number
    print((x+1)," * ", number, " = ", result)
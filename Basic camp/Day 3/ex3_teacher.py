shop_list = list()

for count in range(10):
    item = input("enter a new item: ")

    shop_list.append(item)

    for i in range(len(shop_list)):
        print(shop_list[i])

    answer = input("do you want to continue ")

    if answer == 'no':
        break

answer = input("do you want to remove ")
if answer == 'yes':
    answer = input("what do you want to remove? ")
    shop_list.remove(answer)

print(shop_list)


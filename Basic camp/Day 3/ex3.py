print("Shoppint list")

products = list()
app = True

while app:
    answer = input("Choose add, delete, show or end: ")
    
    if answer == 'add':
            product = input('Enter the product name: ')
            if len(products)< 2:
              products.append(product)
            else:
                print("10 products is max")
    elif answer == 'show':
        print(products)
    elif answer == 'delete':
        delet = input('enter number of delete product name: ')
        products.remove(delet)
    elif answer == 'end':
        app = False
    else:
        print('incorect')
        #app = False



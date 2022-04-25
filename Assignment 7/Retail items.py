# Driver: Khanh Dong (U14837275)
# Navigator: Michael Adam (U62660400)
# Description: The program receive the name, amount and price of 2 items, then print out the receipt.

class Retail_Item:
    def __init__(self, type, number, price):
        self.__type = type
        self.__number= number
        self.__price = price

    def __str__(self):
        format_string = ('{item: <27}{amount: <19}{price: <9}')
        return format_string.format(item = self.__type,amount =self.__number, price = self.__price)

def main():
    
    type1 = str(input("Name of item 1: "))
    amt1 = int(input('Amount of item 1: '))
    price1 = float(input('Price of item 1: '))
    item1 = Retail_Item(type1, amt1, price1)
    
    print(' ')

    type2 = str(input("Name of item 2: "))   
    amt2 = int(input('Amount of item 2: '))
    price2 = float(input('Price of item 2: '))
    item2 = Retail_Item(type2, amt2, price2)

    print(' ')
    print("Here is a summary of the items you added:")
    format_string = ('{item:<27}{amount:<19}{price:<9}')
    print(format_string.format(item = 'Items', amount='Amount', price = 'Price($)'))
    print("-"*55)
    print(item1)
    print(item2)

main()
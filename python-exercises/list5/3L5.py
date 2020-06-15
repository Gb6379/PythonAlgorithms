import random
import time
import os


code = []
price = []

counter1 = 0
counter2 = 0
fulfill = 0


while fulfill < 10:
    code.append(random.randint(1, 100000))
    price.append(random.randint(1, 1000))
    fulfill += 1
print('code list', code)
print('price list', price)

value = int(input("type the product code\n"))

for c in code:  # go over the code list
    if value == c:  # verify if the value gathered exist in the list
        for p in price:  # go over the price list
            # verify the index of the value in code list and print the value assigned to the price list
            if code.index(c) == price.index(p):
                print('code:', c, 'price $', p)
os.system('pause')

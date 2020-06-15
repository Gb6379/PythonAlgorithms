import time
value1 = int(input("Type the first value")) #first element of a aritmetic proggression
value2 = int(input("Type the constant")) #constant

for i in range(1,11):
    value1 = value1 + value2
    print(value1)
time.sleep(11)
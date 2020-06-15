import os
import time
import random

list = []
fulfill = 0
verifying = 0

while fulfill < 10:
    list.append(random.randint(1, 11))
    fulfill += 1
print(list)

value = int(input("Type a value:"))

while (verifying < len(list)):
    if value == list[verifying]:
        print("Value exist, index", verifying)
    else:
        print("Value doesn`t exist")
    verifying += 1
os.system('pause')

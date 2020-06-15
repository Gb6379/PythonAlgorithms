import os
import time
import random

list1 = []
list2 = []
list3 = []
fulfill = 0
i = 0
j = 0

while fulfill < 10:
    list1.append(random.randint(1, 100))
    list2.append(random.randint(1, 100))
    fulfill += 1
print('List 1 values =>', list1)
print('List 2 values =>', list2)
print("unifying")
time.sleep(1)
list1.append(list2)
print('Union between the lists =>', list1)

while (i < len(list1) and j < len(list2)):
    list3.append(list1[i] + list2[j])
    print(list1[i], '+', list2[j], '=', list3[i])
    i += 1
    j += 1
print('Sum of the list`s values =>', list3)
os.system('pause')

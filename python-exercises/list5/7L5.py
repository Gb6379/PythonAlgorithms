import os

dict1 = {}
keep = 0

while 1:
    key = input('Name: ')
    gender = input('Gender: ')
    age = int(input('Age: '))
    health = int(input('health 1(ok) 2(not ok):'))

    dict1[key] = gender, age, health
    keep = int(input('Do you want to keep registering? (1)Y (2)N: '))
    if keep == 2:
        break

if age >= 18:
    print('able to serve', dict1[key])

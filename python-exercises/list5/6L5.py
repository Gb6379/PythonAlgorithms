import os

dict1 = {}
keep = 0

while 1:
    key = input('CPF: ')
    name = input('Name: ')
    height = float(input('Height: '))
    weight = float(input('Weight:'))

    dict1[key] = name, height, weight
    keep = int(input('Do you want to keep registering? (1)Y (2)N: '))
    if keep == 2:
        break

while 1:
    key = input('Type the CPF of the person you want to fetch: ')
    print(dict1.get(key))
    keep = int(input('Do you want to keep consulting? (1)Y (2)N:'))
    if keep == 2:
        break

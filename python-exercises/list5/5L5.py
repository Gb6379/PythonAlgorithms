import os

dict1 = {}

# gather the student information
while 1:
    key = input('name: ')
    value1 = int(input('grade1: '))
    value2 = int(input('grade2: '))
    # input into the dictionary setting the name as a key
    dict1[key] = value1, value2
    keep = int(input('do you want to keel registering? (1)Y (2)N'))
    if keep == 2:
        break

print(dict1)

while 1:
    key = input('Students name: ')
    # get the key(name) informed above and print it's grades
    print('Student grades:', dict1.get(key))
    # assign the grades of the key into a variable
    value = dict1.get(key)
    # makes the mean
    print('Student mean:', sum(value)/2)
    keep2 = int(input('Do you want to keep consulting the grades? (1)Y (2)N'))
    if keep2 == 2:
        break
os.system('pause')

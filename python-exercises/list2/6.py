import time
import os 

M = ["Male"]
F = ["Female"]
AF = 'Infantil A-F'
AM = 'Infantil A-M'
B = 'Infantil B'
A = 'Juvenil A'

name = (input("Type your name  "))
age = int (input("Type your age  "))
gender = int(input("Type (1)M (2)F  "))

if age >= 6 and age <=8:
    if gender == 2:
        print("swimmer belongs to category: %s" %AF)   
    else:
        print("swimmer belongs to category: %s" %AM)

elif age >= 9 and age <=11:
    print("swimer belong to category: %s" %B)
    
elif age >= 12 and age <= 14:
    print("swimmer belongs to category: %s" %A)
else:
    print("There's no classification for your age")

time.sleep(5)
os.system("PAUSE")

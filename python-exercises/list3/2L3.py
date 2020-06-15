import time
value = int(input("Value:"))

i = 2
fat = 1

while i <= value:
    fat = fat * i
    i += 1

print(value, '! is ', fat)
time.sleep(10)
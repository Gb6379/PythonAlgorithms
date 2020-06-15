import time

value1 = float(input("Value 1:"))

value2 = float(input("Value 2:"))

value3 = float(input("Value 3:"))

if value1 < value2 + value3 and value2 < value1 + value3 and value3 < value1 + value2:
    print("It's a triangule")
if value1 == value2 and value2 == value3 and value1 == value3:
    print("Equilatral")
elif value1 == value2 or value2 == value3 or value1 == value3:
    print("isosceles")
elif value1 != value2 and value2 != value3 and value3 != value1:
    print("scalene")
time.sleep(50)

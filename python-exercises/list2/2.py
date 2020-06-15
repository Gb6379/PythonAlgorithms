import time

cordenate1 = float(input("type cordenate 1:\n"))
cordenate2 = float(input("type Cordenate 2:\n"))

area = cordenate1 * cordenate2

print("area %.2f" %area)
if area < 0:
    print("area can't be negative")
time.sleep(50)

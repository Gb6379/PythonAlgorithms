import time
value1 = int(input("First value "))
value2 = int(input("Second value "))

index = int(input("Index: "))

for i in range(value1, value2):
    result = i ** index
    print(i,'^',index,'=',result)
time.sleep(11)

import time
Value = int (input("Type the value of x1:"))
Value2 = int (input("Type the value of x2:"))


for i in range(Value, Value2):
    result = (4*i) + 3
    print('4 x',i,'+ 3 =',result)
time.sleep(11)
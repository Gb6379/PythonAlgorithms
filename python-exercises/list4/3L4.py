import time
import os

A = [1,2,3,4,5,6,7,8,9,10]
B = [10,20,30,40,50,60,70,80,90,100]
C = []
i = 0
j = 0

while (i < len(A)) and (j < len(B)):
    print('calculating lists values')
    time.sleep(0.5)
    C.append(A[i] * B[j])
    print(A[i], 'x' , B[j], '=', C[i] )
    i+=1
    j+=1
print('Results',C)
os.system('pause')
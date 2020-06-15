import time
value = 1000

for value in range (1000, 10000):
   DU = (value % 100)
   #print("Unidade e dezena %d" %DU)
   CM = (value // 100)
   #print("Centena e milhar %d" %CM)
   final = (DU + CM)**2
   if final == value:
        print('the number that fallow the rule are' , final)

time.sleep(51)
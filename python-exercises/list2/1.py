import time

value = int(input("digite um n entre 1000 e 9999\n"))
if value < 1000 or value > 9999:
    print("Invalido")
else:
   DU = (value % 100)
   print("Unidade e dezena %d" %DU)
   CM = (value // 100)
   print("Centena e milhar %d" %CM)
   final = (DU + CM)**2
if final == value:
   print("resultado %d" %final)

else:
    print("Nao se aplica")
time.sleep(50)
for value in range(1000, 10000): #value = 1000 and goes till 10000

    DU = (value % 100)
    #print("Unidade e dezena %d" %DU)
    CM = (value // 100)
    #print("Centena e milhar %d" %CM)
    final = (DU + CM)**2
    if final == value:
        print("resultado %d" %final)

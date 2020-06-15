import time


height = float(input("Type your height:  "))
weight = float(input("Type your weigth:  "))
gender = int(input("Type your gender:(1)M (2)F:  "))


inputValue = "Male" if gender == 1 else "Female"
print(inputValue)

if gender == 1:
    Wcalculation = (72.7 * height) - 58
    if weight > Wcalculation:
        print("Overweigth - landmark: %.2f" %Wcalculation)
    else:
        print("Normal Weigth - landmark: %.2f" %Wcalculation)
else:
    Wcalculation = (62.1 * height) - 44.7
    if weight > Wcalculation:
        print("Overweigth - landmark: %.2f" %Wcalculation)
    else:
        print("Normal Weigth - landmark: %.2f" %Wcalculation)
time.sleep(50)

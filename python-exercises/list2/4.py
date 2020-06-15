import time

salary = float(input("Type your wage\n"))

if salary <= 1566.61:
    print("no taxes applyed")
    
elif salary > 1566.61 and salary <= 2347.85:
    tax = (salary * 7.5)/100
    print("Taxes charged %.2f" %tax)
    
elif salary > 2347.85 and salary <= 3130.51:
    tax = (salary * 15)/100
    print("Taxes charged %.2f" %tax)
    
elif salary > 3130.51 and salary <=3911.63:
    tax = (salary * 22.5)/100
    print("Taxes charged %.2f" %tax)
    
elif salary > 3911.64:
    tax = (salary * 27.5)/100
    print("Taxes charged %.2f" %tax)
time.sleep(50)

import time
import os



classSubject = (input("Type a class you're enroled in: "))
workload = int (input("Type the workload in H: "))
classMissed = int (input("Type the number of class missed: "))

totalWorkload = (workload * 60)
minimalWorkload = (totalWorkload * 25)/100

studentMissedHours = (classMissed*50)

if studentMissedHours > minimalWorkload:
    print("You got reproved by attendance")
    print("The total workload of this class is %d and you missed %d wich is more than 75 percent" %(totalWorkload, studentMissedHours))

gradeOne = float (input("Type your first grade"))
gradeTwo = float (input("Type your second grade"))
gradeThree = float (input("Type your third grade"))

gradeMean = (gradeOne + gradeTwo + gradeThree)/3
if gradeMean >= 6:
    print("Congrats, you have been Aproved on %s !" %classSubject)
    print("Grade: %2.f" %gradeMean)
else:
    print("Shame, you have been Reproved. Try on the next semester :(")
    
time.sleep(3)
os.system("PAUSE")
                

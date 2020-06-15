numLoops = 0
run = True

while run:
   os.system('CLS')
    print("loop %d" %numLoops)
    numLoops += 1
    if numLoops == 20:
        run = False

print("Ending")

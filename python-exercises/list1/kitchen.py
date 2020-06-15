print("Type the length")
length = float (input())
print("Type the width")
width = float (input())
print("Type the height")
height = float (input())

print(" Length: %.2f - Width: %.2f - Height: %.2f" %(length, width, height))
pad = 1.5
area = (length * width)
covering = area/pad
print("Area: %.2f" %area)
print("Amount of pads needed to cover the area %.2f" %covering)
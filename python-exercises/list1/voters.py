print("Type the amount of null voters:")
nullV = float (input())
print("Type the blank amount of voters:")
blank = float (input())
print("Type the valid amount of voters:")
valid = float (input())

overall = valid + blank + nullV
Nullpercentage = (nullV * 100)/overall
blankPercentage = (blank * 100)/overall
validPercentage = (valid * 100)/overall

print("Null: %.2f - Blank: %.2f - Valid: %.2f - Overall: %.2f" %(nullV, blank, valid, overall))
print("Percentage: Null %.2f - Blank: %.2f - Valid: %.2f" %(Nullpercentage, blankPercentage, validPercentage))

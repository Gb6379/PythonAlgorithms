import time
print("Type the invoice value:")
invoice = float (input())
print("invoice %.2f" %invoice)

invoiceReajustment = (invoice*5)/100 * 12 + invoice
print("Your reajustment is %2.f" %invoiceReajustment)
time.sleep(10)
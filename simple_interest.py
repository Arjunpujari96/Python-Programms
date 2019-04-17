# program for calculate the simple interest

p = float(input("Enter the principal"))
r = float(input("Enter the rate% per annum"))
t = float(input("Enter the time"))

SI = (p*r*t)/100
print("Simple Interest is %f" %SI)

"""If you want to calculate the Amount with interest"""
A = SI+p
print("And the amount is ",A)

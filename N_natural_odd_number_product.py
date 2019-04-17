# Program to calculate product of first n Odd natural number, number is taken from user

a = int(input("Enter any number"))
b=1
c=1
while b<=(2*a-1):
    if b%2!=0:
        c=c*b
        b+=1
    else:
        b+=1
print("Product of n Odd numbers is = %d"%c)

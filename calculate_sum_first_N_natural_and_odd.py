# Program to calculate sum of first N natural numbers

a = int(input("Enter any natural number for calculate sum "))
b=1
n=0
c=0
while b<=a:
    c=c+b
    b+=1
print("sum of the Natural number is %d"%c):
    
    
 """********************************************************"""

 #program to calculate sum of first N natural odd number , input is taken from user
    
 a = int(input("Enter any input "))
b=1
n=0
c=0
while b<=a:
    if b%2!=0:
        c=c+b
        b+=1
    else:
        b+=1
print("sum is %d"%c)


    

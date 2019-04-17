#Program to calculate HCF of two number



a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
l = a if a<b else b
for i in range(l,0,-1):
       if a%i==0 and b%i==0:
              print(i)
              break
print("HCF of %d and %d is = %d"%(a,b,i)

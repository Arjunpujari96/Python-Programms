#program to print the power of the number

a = int(input("Enter a number = "))
b = int(input("Enter the power of a number = "))
s=1
for i in range(1,b+1):
        s = s*a
print("%d to the power of %d is %d"%(a,b,s))

#Program to print LCM of two numbers



a = int(input("Enter a first number"))
b = int(input("Enter a second number"))
l = a if a>b else b
for i in range(l+l,a*b+1):
       if i%a==0 and i%b==0:
              print(i)
              break


print("LCM of %d and %d is = %d"%(a,b,i))

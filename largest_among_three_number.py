# Method 1 (using if else)
 
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
if (a>b) and (a>c):
  max = a
elif (b>a) and (b>c):
  max = b
else:
  max = c
  
print("Greatest number is %d" %max)



#***************************************************************#

#method 2 (using list and inbuilt function)

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

ls = [a,b,c]
print("Greatest number is = ", max(ls))


 

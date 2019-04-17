# Method-1 (Using If-else statements)

print("Enter three city names")
a,b,c = input(),input(),input()
x = min(a,b,c)    #in python string comparison is available
print(x)
if x==a:
       print(min(b,c),max(b,c))
elif x==b:
       print(min(a,c),max(a,c))
else:
       print(min(a,b),max(a,b))

       
 """********************************************************************"""

# Method-2 (Using inbuilt function)


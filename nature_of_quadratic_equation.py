# Find the nature of quadratic equation

import math
a = float(input("Enter the cofficient a"))
b = float(input("Enter the cofficient b"))
c = float(input("Enter the cofficient c"))

d = b*b-4*a*c

if d>0:
       r1 = (-b - math.sqrt(d)) / (2 * a)
       r2 = (-b + math.sqrt(d)) / (2 * a)
       print("roots are real and unequal = %f and %f ",%(r1,r2))     
                  
elif d==0:
        r = -b/(2*a)
        print("roots are real of equal = %f",%r)
else:
        print("No real roots are there")

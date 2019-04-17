# N even natural number in reverse order using range function in for loop

a = int(input("Enter number to print odd number"))

# method 1
for b in range((2*a),0,-2):
       print(b)
    
    
# method 2    
for b in range(1,a):
       print(2*a+2-2*b)

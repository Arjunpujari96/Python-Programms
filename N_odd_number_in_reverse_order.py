# N odd natural number in reverse order using range funtion in for loop

a = int(input("Enter number to print odd number"))


#method 1
for b in range((2*a-1),0,-2):
       print(b)


#method 2
for b in range(1,a+1):
       print(2*a-2*b+1)

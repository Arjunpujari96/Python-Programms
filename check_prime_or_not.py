# Program to check number is prime or not


a = int(input("Enter any number to check prime or not"))
if a<2:
  print("Number is not prime")
else:
  for x in range(2,a):
        if a%x==0:
            print("Number is not prime number")
            break
  else:
    print("Number is prime")

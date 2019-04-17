# program to to print the next prime number of the given number

a = int(input("Enter the number"))
while True:
    a+=1
    for b in range(2,a):
            if a%b==0:
                break
    else:
      print("Next prime number of a given number is = %d" %a)
      break

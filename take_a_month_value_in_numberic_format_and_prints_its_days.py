#take a months value in numeric format and print its days

a = int(input("Please enter the months value 1 to 12 "))


    if a<=12 and a%2!=0:
          print("31 days")
    elif a<=12 and (a%2==0 and a!=2):
          print("30 days")
    elif a == 2:
          print("28 days")
    else:
          print("Please enter a valid month value")

# program to calculate sum of all even and all odd in list , list are given by user

list = []
e = 0
o = 0
number = int(input("Enter the length of the list"))
print("Enter the list value")
for i in range(number):
        data = int(input())
        if data%2==0:
                e = e+data
        else:
                o = o+data
        list.append(data)
print(list)
print(" Sum of all even number in list is = %d"%e)
print(" Sum of all odd number in list is  = %d"%o)

# program to calculate sum of all integers in list , list are given by user

list = []
e = 0

number = int(input("Enter the length of the list"))
print("Enter the list value")
for i in range(number):
        data = int(input())
        e = e+data
        list.append(data)
print(list)
print(" Sum of all integers number in list is = %d"%e)


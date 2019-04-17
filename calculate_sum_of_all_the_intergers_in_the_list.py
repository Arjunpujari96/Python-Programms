# program to calculate sum of all the integers of a list, given by user

list = []
number = int(input("Enter the length of the string"))
print("Enter List value")
for i in range(number):
       data = int(input())
       list.append(data)
print("your inserted list is = ", list)
sum = 0
for s in list:
       sum = sum + s
print(sum)



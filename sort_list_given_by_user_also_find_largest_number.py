# Program to sort list value, and list value is take from user

list = []
number = int(input("Enter the length of the string"))
print("Enter List value")
for i in range(number):
       data = int(input())
       list.append(data)
print("your inserted list is = ", list)


#bubble sort algorithms are used
for i in range(len(list) -1 ,0,-1):
       for j in range(i):
              if list[j] > list[j+1]:
                     temp          = list[j]
                     list[j]       = list[j+1]
                     list[j+1]     = temp

print("Sorted list is ", list)
print("Largest number is = ", list[number-1])

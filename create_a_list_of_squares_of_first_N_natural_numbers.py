#program to create list of squares of first N natural numbers,Value of N is taken from user


list = []
len = int(input("Enter the length of the string"))
for i in range(len):
        data = int(input())
        s    = data*data
        list.append(s)
print(list)

#Student marks percentage 

print("Enter the Student subject marks")
h = int(input("Hindi Marks"))
e = int(input("English Marks"))
p = int(input("Physics Marks"))
c = int(input("Chemistry Marks"))
m = int(input("Maths Marks"))

if (h<=100 and e<=100) and (p<=100 and c<=100):
    if m<=100:
        t = h+e+p+c+m
        p = (t/500)*100
        print("Total marks of student %d" % t)
        print("Total percentage of the student %dpercent " % p)
else:
    print("Please enter the valid marks !")



# program to check leap year

y = int(input("Please enter any year")
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
  print("This year is a leap year %d" %y)
else:
  print("This year is not a leap year")

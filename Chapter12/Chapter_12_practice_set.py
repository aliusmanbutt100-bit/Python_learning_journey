# problem no 1: write a program to open three files and if they dont exist then print error
try:
   with open("1.txt","r") as f:
    print(f.read())
except Exception as e:
   print(e)
   print("there is a error in file no1")
try:
   with open("2.txt","r") as f:
    print(f.read())
except Exception as e:
   print(e)
   print("there is a error in file no2")
try:
  with open("3.txt","r") as f:
    print(f.read())
except Exception as e:
   print(e)
   print("there is a error in file no3")
# problem no 2:print the third,fifth and seventh element of list using enumerate function 
l=[1,2,3,4,5,6,7,8]
for i,item in enumerate(l):
  if(i==2 or i==4 or i==6):
    print(item)
# problem no 3:write a list comprehension to print a list which contains the multiplication table of a user entered number
n=int(input("enter the number:"))
table=[n*i for i in range(1,11)]
print(table)
# problem no 4:write a program to handel the zero division error
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if(b==0):
  raise ZeroDivisionError("hey!this program is not meant for zero division")
else:
  print(f"the divisible is: {a/b}")
# problem no 5:store the multiplication table in problem 3 store in a file  table.txt
n=int(input("enter the number:"))
table=[n*i for i in range(1,11)]
print(table)
with open("table.txt","w") as f:
  f.write(f"the table of {n}:{str(table)} \n")

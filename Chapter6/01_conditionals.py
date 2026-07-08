# If elif else ladder
a=int(input("enter your age:"))
if(a>=40):
    print("you are too old for this job")
elif(a<0):
    print("you are entering the wrong age")
elif(a==0):
    print("this is not a valid age")

else:
    print("you are eligible for this job")
# if else statement
a=int(input("enter your age:"))
if(a>=40):
    print("you are too old for this job")
else:
    print("you are eligible for this job")
print("end of program")
# Quiz:write a program to print yes when the age is entered by user is greater than or equals to 18
age=int(input("enter the age:"))
if(age>=18):
    print("yes u r adult enough")
else:
    print("you are not old enough")
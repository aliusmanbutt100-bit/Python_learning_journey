# Qno1:write a program to  find the greatest of four no enter by user
a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
c=int(input("enter the number 3:"))
d=int(input("enter the number 4:"))

if(a>b and a>c and a>d):
    print("a is the greatest no:",a)
elif(b>a and b>c and b>d):
    print("b is the greatest no:",b)
elif(c>a and c>b and c>d):
    print("c is the greatest no:",c)
else:
    print("d is the greatest no:",d)
# Qno2:
marks1=int(input("enter the marks 1:"))
marks2=int(input("enter the marks 2:"))
marks3=int(input("enter the marks 3:"))
#check for total percentage
total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass")
else:
    print("you are failed,try again next year")
# Qno3:'IN' keyword
p1="make a lot of money"
p2="buy now"
p3="subscribe now"
p4="click this"

message=input("enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is a spam")
else:
    print("this comment is not a spam")
# Qno4:print if length of user name is less than 10
user_name=input("enter your name:")
if(len(user_name)<=10):
    print("this username is too short")
else:
    print("all is right!")
#Qno5:check name in list using if
l1=["ali","usman","ahmed","zainab","fatima"]
name=input("enter your name:")
if(name in l1):
    print("your name is in the list")
else:
    print("your name is not present in the list")
# Qno6:
marks=int(input("enter the marks:"))
if(marks>=90):
    print("you get A+ grade")
elif(marks>=80):
    print("you get A grade")
elif(marks>=70):
    print("you get B grade")
elif(marks>=60):
    print("you get C grade")
elif(marks>=50):
    print("you get D grade")
elif(marks<50):
    print("you get Fail")
# Qno7:
post=input("enter the post:")
if("ali" in post.lower()):
    print("this post is talking about ali")
else:
    print("this post is not talking about ali")
#Problem no1:we make two virtual environments,install some packages in the first one then how we do for sec environment
#first make two virtual environments by using command:
    #py -m venv env1
    #py -m venv env2
#now to activate any of them we use this command:
   # env1\Scripts\activate
#now install some packages by using command:
   # py -m pip install pandas
   # py -m pip install pyjokes
#now we use this command to generate a requirement file(it tells about downloaded packages)
   # py -m pip freeze  (it tell the info about packages)
   # py -m pip freeze > requirements.txt  (it generate the file of the info about packages)
#now we activate the sec virtual environment so we have to deactivate the first
    # deactivate (it deactivates)
#now we use the same command to activate env2:
    # env2\Scripts\activate
#now to copy all the packages of ev1 in ev2 we write command:
   # pip install -r .\reqirements.txt
#now u can check such as import pandas that i also copy in env2

#Problem no2:write a program to input name,marks,phone no of stu and format it using format function
name=input("enter name:")
marks=int(input("enter marks:"))
phoneno=int(input("enter phone no:"))
s="the name of the student is:{0},the marks of the student is:{1},the phoneno of the student is:{2}".format(name,marks,phoneno)
print(s)
#Problem no3:a list contains multiplication table of 7.write a program to convert it to the string of same numbers
table=[str(7*i) for i in range(1,11)]   #here we use comprehension list function
str(table)
s="\n".join(table)
print(s)
#Problem no4:filter a list of numbers which are divisible by 5
def divisible5(n):
    if(n%5==0):
        return True
    return False
a=[23,424,45,50,5,23234]
f=filter(divisible5,a)
print(list(f))
#Problem no5:program to find maxium no in list by reduce function
from functools import reduce
l=[23,424,45,50,5,23234]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l))
#Problem no6:on another file




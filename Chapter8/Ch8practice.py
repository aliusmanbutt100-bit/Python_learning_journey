# Qno1:find the greatest using function 
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
print(f"the greatest number is:{greatest(a,b,c)}")
#Qno2:program to convert Celcius to Fahrenheit using function
# th formula of this is:
# c=5*(f-32/9) 
def convert(f):
   return 5*(f-32/9) 
f=int(input("enter the temperature:"))
print(f"the fahrenhiet is:{convert(f)}")
#Qno3:prevent new line in python
print("a")
print("b")
print("c",end="")  #so this end="" avoid new line
print("d")
# Qno4:write a recursive funtion to sum the first ten natural numbers
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(4))
#Qno5:Draw the pattern with recursion
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1) 
pattern(5)
#Qno6:program function to convert inches to Cm 
def inch_cm(inch):
    return inch*2.54
inch=int(input("enter the value in inches:"))
print(f"the value in cm is:{inch_cm(inch)}")
#Qno7:funtion to remove given word from a list and strip it at the same time
l1=["ali","usman","umar","ant"]
def remove(l1,word):
    l1.remove(word)
    return l1
print(remove(l1,"ant"))
#Qno8:python function to write multiplication table
def mul_table(n):
    mul=1
    for i in range(1,11):
     print(f"{n} x {i} = {n*i}")
mul_table(5)

i=1
while(i>=0):
    print

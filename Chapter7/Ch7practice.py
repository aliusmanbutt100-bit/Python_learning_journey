#Qno1:write a multiplication table of a given number
n=int(input("enter the digit:"))
for i in range(1,11):
    print(f"{n} X {i}= {n*i}")    #we use 'f' string it allow to write integers in it
#Qno2:program to greet all person in the list and starts with S
l=["ali","suman","subhan","sulman","saleem","hareem","hassan"]
for name in (l):
    if(name.startswith("s")): 
     print(f"Hello:,{name}")
#Qno3:program to check prime number
n=int(input("enter the number:"))
for i in range(2,n):
   if(n%i)==0:
      print("this is not a prime number")
      break
   else:
     print("this is a prime number")
     break
#Qno4:program to sum n natural number using while loop
n=int(input("enter the number:"))
i=1
sum=0
while(i<=n):
   sum +=i
   i+=1
print(sum)
#Qno5:factorial of a given number using for loop
n=int(input("enter the number:"))
mul=1
for i in range(1,n+1):
   mul=mul*i
print(f"the factorial of {n} is {mul}")
#Qno6:print star programs
n=int(input("enter the number:"))
for i in range(1,n+1):
   print(" "* (n-1), end=" ")
   print("*"* (2*i-1), end=" ")
   print("")
#Qno7:print star program
n=int(input("enter the number:"))
for i in range(1,n+1):
   print("*"* i, end=" ")
   print("")
#Qno:program to print miltiplication table of n using for loops in reversed order
n=int(input("enter the digit:"))
for i in range(1,11):
    print(f"{n} X {11-i}= {n*(11-i)}") 
   
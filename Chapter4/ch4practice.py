# Qno1:enter 4 fruit names in a list 
fruits=[]
f1=input("enter the fruit name:")
fruits.append(f1)
f2=input("enter the fruit name:")
fruits.append(f2)
f3=input("enter the fruit name:")
fruits.append(f3)
f4=input("enter the fruit name:")
fruits.append(f4)
print(fruits)
#Qno2:enter the marks of student by user and sort them
marks=[]
f1=int(input("enter the marks:"))
marks.append(f1)
f2=int(input("enter the marks:"))
marks.append(f2)
f3=int(input("enter the marks:"))
marks.append(f3)
f4=int(input("enter the marks:"))
marks.append(f4)
marks.sort()
print(marks)
#Qno3:sum list of 4 numbers
l1=[1,6,4,7]
print(sum(l1))
#Qno4:count no of zero in a tuple
a=(3,4,0,20,2,0,2,5,0)
c=a.count(0)
print(c)
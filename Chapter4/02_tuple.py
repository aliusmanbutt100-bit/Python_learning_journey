a=(1,3,5,4)  #Tuple is also immutable as string
print(type(a))
b=() #empty tuple
print(b)
c=(1,)   #tuple with single element
print(type(c))
# Tuple Methods
d=(1,34,54,45,False,"ali")
no=d.count(45)  #count value in tuple
print(no)
 
index=d.index(54)  #tell index of a value
print(index)

print(len(d))   #length of tuple
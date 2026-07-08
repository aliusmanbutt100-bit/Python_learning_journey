e=set()          #dont use s={} as it will create an empty dictionary not empty set 
print(type(e))

s={1,40,5,4,3,5,1,5}  #it does'nt print repeat values
print(s)
# Methods of Sets
s={1,40,5,4,3,5,1,5} 
s.add(56)
print(s,type(s))

print(len(s))

s.remove(1)
print(s)

print(s.pop())

# s.clear()
# print(s)

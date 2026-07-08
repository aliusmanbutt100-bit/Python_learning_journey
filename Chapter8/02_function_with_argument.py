def greet(name,ending):
    print("Good day,"+name)
    print(ending)
    return "ok"       #return sy function ki value a mei jai gi

a=greet("ALi","thank u")
print(a)
# default parameter
def greet(name,ending="byeee!"):
    print("nice to meet u",name)
    print(ending)
greet("Ali")
#func to sum two num
def sum(a,b):
    print(a+b)
    return
sum(10,20)

l=[2,4,4,5]
def remove(l,word=2):
    l.remove(word)
    return l
print(remove(l,2))

#multi-level inheretance-----> when child become parent class for another child class
class employee:
    a=1
class programmer(employee):
    b=2
class manager(programmer):  #manager become the child of a child class
    c=3
o=programmer()
print(o.a,o.b)
o=manager()
print(o.a,o.b,o.c)
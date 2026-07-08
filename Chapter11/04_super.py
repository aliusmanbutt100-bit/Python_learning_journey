class employee:
    a=1
    def __init__(self):
        print("constructor of employee")
class programmer(employee):
    b=2
    def __init__(self):
        print("constructor of programmer")
class manager(programmer):  #manager become the child of a child class
    c=3
    def __init__(self):
        super().__init__()       #it runs the constructor of its parent also
        print("constructor of manager")
o=programmer()
print(o.a,o.b)
o=manager()
print(o.a,o.b,o.c)
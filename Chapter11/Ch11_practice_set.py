#Problem no1: make a 2-D vector class that represent 3-D vector
class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector is: {self.i}i+{self.j}j")
class threedvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"the vector is: {self.i}i+{self.j}j+{self.k}k")
o=twoDvector(1,2)
o.show()
p=threedvector(1,2,3)
p.show()
# Problem no2:create a class pet from dog and further create a class dog from pets.Add a method bark to class dog 
class Animals:
    pass
class pets(Animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("the dog is barking Bow Bow!")

d=dog()
d.bark()
#Problem no3:create a class employee and increment properties to it
class employee:
    salary=234
    increment=20
    @property
    def salaryAfterincrement(self):
        return(self.salary+self.salary*(self.increment/100)) 
e=employee()
print(e.salaryAfterincrement)
#Problem no4:write a class complex to represent complex numbers,along with overloaded operator which add and mulyiples them
class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
c1=complex(1,2)
c2=complex(3,4)
print(c1+c2)
# Problem no5:Addition in vector
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,other):
        return vector(self.i+other.i,self.j+other.j,self.k+other.k)
    def __str__(self):  #str method is use so it can print it correctly
        return f"vector({self.i},{self.j},{self.k})"
V1=vector(2,3,5)
V2=vector(1,2,3)
print(V1+V2)
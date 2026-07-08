#problem no 1: make a class and store information of programmers working in micro
class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
p=programmer("Ali","1500000",25359)
print(p.name,p.salary,p.pin,p.company)

#problem no 2:write a class "calculator" capable of finding square,cube,square root of s number
class Calculator:
    def __init__(self, n):  #use double underscore
        self.n = n

    def square(self):
        print(f"the square is:{self.n*self.n}")

    def cube(self):
        print(f"the square is:{self.n*self.n*self.n}")

    def sqroot(self):
        print(f"the square is:{self.n**1/2}")
    @staticmethod
    def heloo():
        print("this is our calculator")

a = Calculator(4)
a.square()
a.cube()
a.sqroot()
a.heloo()

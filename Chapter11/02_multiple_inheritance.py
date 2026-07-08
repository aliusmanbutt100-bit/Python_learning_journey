#here in multiple one child can have more than one parent class
class employee:
    company="ITC"
    salary=120000000
    def show(self):
        print(f"the name is:{self.company} and the salary is:{self.salary}")
class coder:
    language="Python"
    def printlanguage(self):
        print(f"out of all languages here is your language:{self.language}")

class programmer(employee,coder):   #so this is the syntax and it means the programmer is the child class of employee and coder
    company="ITC Infotech"
    def showlanguage(self):      #all the attributes and method is automatically copy in child class of both parent classes 
        print(f"His name is:{self.company} and he is good with {self.language} language")

# a=employee()
b=programmer()        #so see we can simply use method of parents class with object of child
b.printlanguage()
b.showlanguage()
b.show()
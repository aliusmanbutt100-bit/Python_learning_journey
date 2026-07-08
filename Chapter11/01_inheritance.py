class employee:
    company="ITC"
    name="Ali"
    salary=120000000
    def show(self):
        print(f"the name is:{self.name} and the salary is:{self.salary}")

# class programmer: 
#       company="ITC Infotech"
#       def show(self):
#         print(f"the name is:{self.name} and the salary is:{self.salary}")
#       def showlanguage(self):
#          print(f"His name is:{self.name} and he is good with{self.language} language")
# so instead of do this we use inheritance
class programmer(employee):   #so this is the syntax and it means the programmer is the child class of employee
    company="ITC Infotech"
    language="Python"
    def showlanguage(self):      #all the attributes and method is automatically copy in child class and so if we need to add any method or do any change the we to it in it as we add new method language and add company name
        print(f"His name is:{self.name} and he is good with {self.language} language")

a=employee()
b=programmer()
print(a.company,b.company)
b.show()
b.showlanguage()

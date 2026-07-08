#here we learn about self parameter/static method
class employee:    #this is a class
    language="python"
    salary=1000000

    def getinfo(self):   #method/function in class/we have to use self its imp
        print(f"the language is {self.language}.the salary is {self.salary}")
    
    @staticmethod   #in static method we dont have to use self
    def greet():
        print("Good morning jani")


lol=employee()   #lol is a object here
lol.language="Javascript"     #instance attribute is preffered over class as we see in case of language
lol.getinfo()   #call method/function
print(lol.salary,lol.language) 
lol.greet()  
#here we learn about Constructor  
class employee:    #this is a class
    name="ali"
    language="python"
    salary=1000000

    def __init__(self,name,language,salary):   #init is a dunder method which is automatically call
        self.name=name
        self.language=language
        self.salary=salary
        print("i am a init method and u dont need to call me")
        print(f"the name is:{name},the language is:{language},the salary is:{salary}")



lol=employee("ALI","Java",1200000)   #lol is a object here



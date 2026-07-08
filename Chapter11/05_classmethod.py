#the classmethod prioritize the value of class attributes instead of object attribute
class school:
    a=1
    @classmethod
    def show(cls):
     print(f"the value of a of class is:{cls.a}")

e=school()
e.a=45
e.show()







class employee:
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


obj=employee()
obj.name="Ali Usman"
print(obj.fname,obj.lname)

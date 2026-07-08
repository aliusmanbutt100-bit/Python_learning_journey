
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
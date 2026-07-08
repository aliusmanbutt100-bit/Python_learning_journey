class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num):       #can also use sub,mul,truediv
        return self.n+num.n
n=number(4)
m=number(2)
print(n+m)



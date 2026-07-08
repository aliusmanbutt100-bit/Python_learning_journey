a=int(input("enter the num:"))
b=int(input("enter the sec num:"))
if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by zero")
else:
   print(f"the division of a/b: {a/b}")

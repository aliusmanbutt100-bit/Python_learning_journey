# Qno1:user input name followed by good afternoon
name=input("enter your name")
print(f"Good Afternoon,{name}")
# Qno2:write a program to detect double space in string
name="ali usman  butt"
print(name.find("  "))
# Qno3:replace the double space with single space
name="ali usman  butt"
print(name.replace("  "," "))
print(name) #strings are immutable which means that you cannot change them by running functions on them
# Qno4:format the following character using espace sequence character
letter="Dear ali,\nthis python course is nice\nthanku!"
print(letter)
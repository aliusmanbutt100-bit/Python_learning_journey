# Functions of String(use chatgpt to discover more)
name="ali usman"
print(len(name))
print(name.endswith("ny"))  
print(name.startswith("al"))
print(name.capitalize())    #only capitalize first character of string
print(name.title())        #capitalize first character of all words in a string 
print(name.lower())        #converts all characters in a string to lowercase
print(name.upper())        #converts all characters in a string to uppercase
print(name.find("a"))      #find a at '0' index
print(name.replace("usman","butt"))   #replace word in string
#escape sequence characters
a="ali is a good boy\n but not a bad \t\"boy\""    #'\n' use to add new line and '\t' give same as tab and \"\" to add doubble quotes
print(a)
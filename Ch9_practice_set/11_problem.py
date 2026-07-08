# how to rename a file in python 
with open("old.txt","r") as f:
    content=f.read()
with open("rename.txt","w") as f:
    f.write(content)
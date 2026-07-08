f=open("file.txt","r")
print(f.read())
f.close()
# the same can be wrriten using with statement like this:
with open("file.txt") as f:
    print(f.read())
    # now u dont need to close the file explicitly

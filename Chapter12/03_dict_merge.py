# in this we can merge two dictionary
dict1={"a":1,"b":2,"c":3}
dict2={"d":1,"e":2,"f":3}
merged=dict1|dict2
print(merged)
#another topic multiple context manager
with(
    open("file1.txt") as f1,
    open("file2.txt") as f2  
): 
  content1=f1.read()
  print(content1)
  content2=f1.write("file.write")


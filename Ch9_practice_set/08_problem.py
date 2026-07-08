# to check if the two files are identical

with open("file.txt","r") as f:
    content1=f.read()
with open("poem.txt","r") as f:
    content2=f.read()
if(content1==content2):
    print("yes both files are identicals")
else:
      print("no both files are not identicals")
  

#check now in which line the word python is:

with open("logfile.txt.html","r") as f:
    content=f.readlines()
lineno=1
for line in content:
  if("python" in content):
    print(f"yes!the word python is present in it in {lineno}")
    break
  lineno +=1

else:
    print("no!the word python is not present in it")




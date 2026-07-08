# check if a log file have python in it or not
with open("logfile.txt.html","r") as f:
    content=f.read()
if("python" in content):
    print("yes!the word python is present in it")
else:
    print("no!the word python is not present in it")

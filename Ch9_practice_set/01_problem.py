# read the twinkle file and check if twinkle word exists
f=open("poem.txt","r")
data=f.read()
if("twinkle" in data):
    print("the word twinkle is present in the content")
else:
    print("the word twinkle is not present in the content")
f.close()
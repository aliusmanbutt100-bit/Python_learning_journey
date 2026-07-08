# replace bad words with "######" same as problem no 4
words=["Donkey","ganda","dalla"]

with open("file.txt","r") as f:
    content=f.read()

for word in words:
 content=content.replace(word,"#" * len(word))

with open("file.txt","w") as f:
    f.write(content)
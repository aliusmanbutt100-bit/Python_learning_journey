#see question on pdf of code with harry
#Qno1:make a dictionary and user can see up it
words={
  "madad":"help",
  "kursi":"chair",
  "billi":"cat"
}
word=input("enter the word u want meaning of:")
print(words[word])
#Qno2:write program to display unique no after input
s=set()
n=input("enter the number 1:")
s.add(int(n))
n=input("enter the number 2:")
s.add(int(n))
n=input("enter the number 3:")
s.add(int(n))
n=input("enter the number 4:")
s.add(int(n))
n=input("enter the number 5:")
s.add(int(n))
n=input("enter the number 6:")
s.add(int(n))
n=input("enter the number 7:")
s.add(int(n))
n=input("enter the number 8:")
s.add(int(n))
print(s)
#Qno3:can we a set of 18(int) and'18'(str) as a value in it
s=set()
s.add(18)
s.add("18")
print(s) 
#Qno4:create an empty dictionary, allow 4 frnds to enter their favourite languages
d={}
name=input("enter the friends name:")
lang=input("enter the language name:")
d.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language name:")
d.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language name:")
d.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language name:")
d.update({name:lang})
print(d)
#Qno5:can u change the value of list which is contained im set S
S={5,"Ali",12,4,[1,3]}
# u cant change bcz u cant have list inside a Set 

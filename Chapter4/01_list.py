# python lists is a container store set of value (of any datatype
friend=["apple","orange",5,345.05,False,"ali","usman"]
print(friend[0])
friend[0]="grapes"    #unlike strings lists are mutable(list can change)
print(friend[0])
print(friend[1:4])
friend.append("suman")  #use to add at the end of the list
print(friend)

l1=[1,5,4,6,7,2]   
l1.sort()            #use to sort the list
print(l1)

# l1.reverse()       #use to reverse the list
# print(l1)
 
l1.insert(2,3)     #this add 3 at index '2'
print(l1)

l1.pop(3)        #delete value at index '3'
print(l1)

l1.remove(7)   #remove value 7 in the list
print(l1)
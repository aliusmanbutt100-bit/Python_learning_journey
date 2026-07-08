s1={1,45,6,78}
s2={7,8,1,78}
print(s1.union(s2))        #to take union
print(s1.intersection(s2))    # to take intersection
print({1,45}.issubset(s1))     #use for subset(means this values are must in our set)
print(s1.issuperset({78,1})) 
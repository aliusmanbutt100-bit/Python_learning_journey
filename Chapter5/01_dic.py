# dictionary is a collection of key-value pairs
#it is mutable als0
marks={
    "Ali":100,
    "Suman":90,
    "Usman":50
}
print(marks,type(marks))
print(marks["Ali"])
# some methods of dictionary
marks={
    "Ali":100,
    "Suman":90,
    "Usman":50,
    0:"Hassan"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ali":99,"Umar":40})
print(marks)
print(marks.get("Ali"))
print(marks.popitem())
print(marks.pop("Ali",any))
print(len(marks))
print(marks)
#Empty Dictionary
d={}
print(type(d))
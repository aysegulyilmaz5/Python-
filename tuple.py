#creating tuple
mytuple=("apple","banana","cherry")
print(mytuple)

#access tuple items
print(mytuple[1])

print(mytuple[0:2])

#changing tuple items
#by default tuple does not allow you change values bacuse it is immutable
#but there is workaround
#tuple --> list(modify) --> tuple
mytuple=("apple","banana","cherry")
mylist=list(mytuple)
mylist[0]="orange"
mytuple = tuple(mylist)
print(mytuple)
print(len(mytuple))

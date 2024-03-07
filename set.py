#create set
myset = {"apple","banana","cherry"}
print(myset)

#accessing items from set
for i in myset:
    print(i)
print("apple" in myset)

#adding items to set
#add()-> add single item  update()-> add multiple items
myset.add("orange")
print(myset) #{'cherry', 'orange', 'banana', 'apple'}
myset.update(["mango","grapes"])
print(myset) #{'orange', 'mango', 'apple', 'grapes', 'banana', 'cherry'}

print(len(myset))

#remove item from set
myset.remove("banana")
print(myset) #{'apple', 'mango', 'cherry', 'grapes', 'orange'}
#myset.remove("xyz") #KeyError:'xyz'

myset.discard("banana")
print(myset) #{'orange', 'grapes', 'mango', 'apple', 'cherry'}

#clear all items from set
myset.clear()
print(myset) #set()

#joining 2 sets - union()
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3) #{1, 'a', 2, 'c', 3, 'b'}

#update()
set1={"a","b","c","d"}
set2={1,2,3}
set1.update(set2)
print(set1) #{1, 2, 'a', 'b', 3, 'c', 'd'}

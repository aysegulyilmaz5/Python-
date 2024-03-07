#mylist = [1,2,3,23,34,45,67]
#mylist2 = ["banana","apple","cherry"]
#mylist3=["apple",1,"banana",2]
#mylist4= list() #empty list

#print(mylist)
#print(mylist2)
#print(mylist3)
#print(mylist4)

#Accessing items from the list
mylist5= ["apple","banana","cherry"]
print(mylist5[0])
print(mylist5[2])

#Range of indexes
mylist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(mylist[2:5])

#change item value
mylist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
mylist[0]="orange"
mylist[1]="avocado"
print(mylist)

#read the list items using loop
mylist= ["apple","banana","cherry"]
for i in mylist:
    print(i)

#check if the item is exist in the list or not
    
if "apple" in mylist:
    print("yes,apple is present")
else:
    print("No apple is not present")

#Add items append() insert()
mylist.append("watermelon") #adding new item at the end of the list
print(mylist)  

mylist.insert(1,"kiwi")
print(mylist)

#remove item from the list
#pop()
mylist.pop(0)
print(mylist)

#clear()
mylist.clear()
print(mylist)

#copy list
mylist1=["apple","banana","cherry"]
mylist2 = list(mylist1)

print(mylist1)
print(mylist2)

#copy()
mylist2=mylist1.copy()

#combine/join lists
#using + operator

list1 = ["a","b","c"]
list2=[1,2,3]
list3= list1 + list2
print(list3)

#using loop statement
for i in list2:
    list1.append(i)
print(list1)

#using extend
list1.extend(list2)
print(list1)
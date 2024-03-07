#creating dictionary
mydic={101:"x:",102:"y",103:"z"}
print(mydic)
print(type(mydic)) #{101: 'x:', 102: 'y', 103: 'z'}
                    #<class 'dict'>

#access items from dictionary
mydic={
    "brand":"Hyundai",
    "model":"i8",
    "year":2021
}

print(mydic["brand"]) #Hyundai

#using get()
x=mydic.get("model")
print(x) #i8

#change values in dictionary
mydic["year"]=2023
print(mydic) #{'brand': 'Hyundai', 'model': 'i8', 'year': 2023}

#reading dictionary using for loop

for i in mydic:
    print(i) #brand
            #model
            #year
    
for i in mydic:
    print(mydic[i]) #Hyundai
                    #i8
                    #2023
    
for i in mydic.values():
    print(i) #Hyundai
            #i8
            #2023
    
for x,y in mydic.items():
    print(x,y)
#brand Hyundai
#model i8
#year 2023
    

#adding items to dictionary
mydic["color"] = "red"
print(mydic) #{'brand': 'Hyundai', 'model': 'i8', 'year': 2023, 'color': 'red'}

#remove items from dictionary
mydic.pop("year")
print(mydic) #{'brand': 'Hyundai', 'model': 'i8', 'color': 'red'}

#copying dictionary
mydic2=mydic
print(mydic2)

mydic2=mydic.copy()
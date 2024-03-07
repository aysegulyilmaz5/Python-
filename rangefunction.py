#range():values between the range

#print(list(range(10)))

#List is another function which will get the values within
#this particular range.

#print(list(range(5,10)))

#print(list(range(1,10,3)))

#print(list(range(10,1,-1)))

i=10
while i>=1:
    print(i)
    i=i-1

for i in range(10):
    print(i)

for i in range(1,10):
    if i==5:
        continue
    print(i)
print("program exited!!")
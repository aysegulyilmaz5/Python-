# class MyClass:
#     def myfunc(self):
#         pass
#     def display(self,name):
#         print(name)

# MyClass() #This is an object

# mc= MyClass()
# mc.myfunc()
# mc.display("Scott") #John

# class MyClass:
#     def m1(self):
#         print("this is an instance method")
#     def m2(self,num):
#         print(num)

# class MyClass:
#     a,b=10,20
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)

# Myc = MyClass()
# Myc.add()
# Myc.mul()


# i,j=15,25 #global variables
# class MyClass:
#     a,b=10,20 #class variables
#     def add(self,x,y): #x,y are local variables
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)

# mc1=MyClass()
# mc1.add(100,200)

a,b=15,25
class MyClass:
    a,b=10,20
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b) #class variables
        print(globals()['a']+globals()['b']) #access global variables
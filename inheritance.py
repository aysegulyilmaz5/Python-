# class A:
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
# bobj = B()
# bobj.m1() #this is m1 method from class A
# bobj.m2()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x + self.y)
# class B:
#     a,b = 200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)

# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# class A:
#     def m1(self):
#         print("This is m1 method from class A")
    
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")
#         super().m1()
# bobj = B()
# bobj.m1() #This is m1 method from class B
# #This is m1 method from class A

# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
# bobj = B()
# bobj.m(1000,2000) #3000
# 300
# 30

class Parent:
    name="Scott"
class Child(Parent):
    name="John"
cobj = Child()
print(cobj.name)
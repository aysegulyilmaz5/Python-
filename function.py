def myfun():
    print("hello")
    
myfun() #call the function

def myfun(name):
    print("Hello",name)

myfun("Ayşegül") #Hello Ayşegül

def cal(a,b):
    return (a+b)
sum=cal(10,20)
print(sum)

global_var =20

def fun():
    local_var = 10
    print(local_var)
    print(global_var)

fun()

#print(local_var) #invalid because local_var is local variable of fun()
print(global_var)

x=100

def cool():
    global x
    x=500
    print(x)
cool()
print(x)

def func(i,j):
    print(i,j)
func(10,20) #Positional arguments

func(j=20,i=10) #Keyword aparameters

#default values assigned to positional arguments
def func(i,j=10):
    print(i,j)
func(100,200)
func(100) #100 10
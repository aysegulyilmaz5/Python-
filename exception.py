#Example1

# print("This is starting point of program...")
# print("This is starting point of program...")
# print("This is starting point of program...")

# try:
#     print(x)
# except:
#     print("Exception occured")

# print("this is end of the program...")
# print("this is end of the program...")
# print("this is end of the program...")

# print("This is starting point of program...")
# print("Program in progress")
# try:
#     print(10/5)
# except ZeroDivisionError:
#     print("Exception occured...handled...")

# print("Program completed")

#Multiple except blocks - try,except else, finally
# try:
#     num1,num2=10,0
#     result=num1/num2
#     print("result is:",result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception")
# except SyntaxError:
#     print("Thrown Syntax error exception...")
# except:
#     print("Exception handled")
# else:
#     print("No exception occured...")
# finally:
#     print("always execute...")

#Raising our own exceptions

def enterage(num):
    if num <0:
        raise ValueError("Only Integers are allowed")
    if num %2==0:
        print("even")
    else:
        print("odd")

print("checking number is even or odd by calling funciton")

num = -1
try:
    enterage(num)
except ValueError:
    print("ValueError exception occured and handled")

print("program completed")
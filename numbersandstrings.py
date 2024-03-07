num1=100
num2=10.5

print(type(num1))
print(type(num2))

print(max(10,20,30))
print(min(13,30,42,57,68,23,14,53,67,78))

#ways of creating string variables
s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome")

#creating empty strigngs
name=""
name=''
name=str()

str1="welcome"
print(id(str1)) #2272176413440
str1=str1 + "to pyhton"
print(id(str1)) #1969232428144

str="welcome"
print(str*3)

print(ord('A'))
print(chr(65))

s="welcome"
print("come" in s)
print("lome" not in s)

print("arrow" > "aron")

print("welcome".isupper())

s="welcome to python"
print(s.endswith("thon"))
print(s.startswith("good"))
print(s.find("come"))
print(s.count("o"))

y="String in PYTHON"

y=y.lower()
print(y)

a="hello"
rev_str=""
for i in a:
    rev_str= i+rev_str
print("reversed string is:",rev_str)

rev_str[::-1]
print(rev_str)
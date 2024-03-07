#Example1: writing data in to text file
#we have to pass two parameters. One is location of the file, and the second parameters is the mode.
#Mode is the reading or writing or append.
# file=open("C:/Users/10132593/Desktop/example.txt",'w')
# file.write("Ntt data business solutions\n")
# file.write("test and business analysis trainees")
# file.close()
# print("program completed")

#Reading data from text file

# file= open("C:/Users/10132593/Desktop/example.txt",'r')
# print(file.read())
# file.close()

#Appending data into text file

file= open("C:/Users/10132593/Desktop/example.txt",'a')
file.write("this test situation1\n")
file.write("this is test situation2\n")
file.close()
print("program is completed")
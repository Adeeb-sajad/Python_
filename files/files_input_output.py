# THe next two lines tell us where python is looking to get the file from 
import os
print("Python is looking at ",os.getcwd())

# READING AND OPENING A FILE - bacha way and pythonic way

# Bacha way of doing FILE I/O in python 
f = open(r"D:\CSE\python\files ka kessa\demo.txt","r")# r - raw string(tells python not to
data = f.read()                                       #     misread our path for escape sequnces like /f etc  
print(data)
print(f"Type of data is {type(data)}")

# Pythonic way of FILE I/O - using [ with ... as ... ] - context manager 

with open(r"D:\CSE\python\files ka kessa\demo.txt","r") as f:
    data = f.read()                                    # read(no of char we wanna read)
    print(f"""The data in the file"demo.txt is - {data}""")

# .readline() - reads one line at a time
with open(r"D:\CSE\python\files ka kessa\demo.txt","r") as f:
   data = f.readline()
   print(f"The line read by readline() is - {data}")

   

# Here no readline nor read needed to print
with open(r"D:\CSE\python\files ka kessa\demo.txt","r") as f:
 for x in f :
    print(x,end="")

# WRITINNG INTO A FILE 

# using "w" which truncates the file first then writes to it  
with open(r"D:\CSE\python\files ka kessa\demo.txt","w") as f:
   input_Str = input("Enter what you wanna write in the file :")
   f.write(input_Str) 


# using "a" which appends to the file
with open(r"D:\CSE\python\files ka kessa\demo.txt","a") as f:  
   input_Str = input("Enter what you wanna append in the file :")   
   f.write(input_Str)

# using "x" which creates the file then write into it 
with open(r"D:\CSE\python\files ka kessa\created_by_x.txt","x") as f:
   input_Str = input("""Enter what you wanna write using "x" in the file :""")   
   f.write(input_Str)
# WHILE LOOP
if 0 :
 i = 0
 while i<5:
     print("hello",i)
     i+=1

#QUESTIONS
if 0 :
# 1) print mul table of n 

 n = int(input("Enter number:"))
 i = 1
 while i<=10 :
    print(n ,"x",i,"=",i*n)
    i=i+1

# 2) print squares of n numbers
 n = int(input("Enter number:"))
 i = 1
 while i<=n :
   print("Square of",i,"=",i**2)
   i=i+1     

# 3) scearch element in a tuple
x = int(input("Enter number: "))
mytuple = (1,4,9,16,25,36,49,64,81,100)
i=0
#while i < len(mytuple):
#   if x == mytuple[i]:
#    print("Found at index",i)
#    break
#   i=i+1 
# 
#if i == len(mytuple) :
#  print("Not in tuple")   

if x in mytuple :
   print("Found at index",mytuple.index(x))
else :
  print("not found")

# FOR LOOPS

mylist = [1,2,3,"meh"]

for el in mylist :
  print(el)         #Prints the element of the list,same for tuple
else :
  print("End of list")

print("\n")

myset = {1,2,"meh",2}
print(type(myset))
for el in myset :
  print(el)  
else :
  print("End of set")  

#range(start,stop,steps)
for el in range(1,5):
  print(el)  
        
#LIST - ordered ,mutable ,allows duplicates, can store different types of data 
#       (heteregenous data can be stored)
# It is both a data type and a data structure 

# Steps to make a list from human friendly data ->
#  1. Convert ,2. seperate (data with commas) ,3.Surround (here with [])
#  4. Assign

# No need to mention it is a list ,the [] tells the PVM that it is a list 
  
#SYNTAX
if 0:
  list_name = [1,"hello",True]
  list_name[0] = 2             # ALLOWED - HENCE MUTABLE
  print(list_name[-1])         # negative indexing allowed OUTPUT: True

# FUNCTIONS 
  # print(), .append() , .insert() , .pop(), .remove(), .clear(), .reverse() , .sort()
  # sorted(mylist), isinstance(), split()

# 1.append() - adding a single item to the end of the list 
 
# 2.extend() - adds a collection of items to the end of the list 

# 3. remove() and insert() - we can specify the location
#                            of insertion and deletion from the list 

# SYNTAX - remove(what to remove) , insert( where to insert , what to insert )

# 4. isinstance() - return true if both the two arguments ka type match
#                   eg : isinstance(mylist,list)
#                        here if mylist is of list type then the isinstance() returns
#                        true



# Ways to copy lists in python (these things apply to all the shit) 
# USING "="
if 0:
 org_list = ["apple","orange","banana"]
 copy_list = org_list        # But this has a problem if we make a change to the copy_list
 copy_list.append("masla")   # the change is applied to the org_list as well 
 print("This is the original list" , org_list)
 print("This is the copied list"  ,copy_list)

#USING .copy()
if 0:
  org_list = ["apple","orange","banana"]
  copy_list = org_list.copy()      
  copy_list.append("masla")    #this doesnt have the above problem
  print("This is the original list" , org_list)
  print("This is the copied list"  ,copy_list)

#USING list()
if 0:
  org_list = ["apple","orange","banana"]
  copy_list = list(org_list)  
  copy_list.append("masla")    #this also doesnt have the above problem
  print("This is the original list" , org_list)
  print("This is the copied list"  ,copy_list)

#USING SPLICING 
if 0:
  org_list = ["apple","orange","banana"]
  copy_list = org_list[:] 
  copy_list.append("masla")    #this also doesnt have the above problem
  print("This is the original list" , org_list)
  print("This is the copied list"  ,copy_list)
    
#List comprehension - making a new list in a single line
if 0:
  mylist = [1,2,3,4,5,6,7]
  b = [ i+1 for i in mylist]     #Here the "i+1" can be any expression 
  print("Original list ",mylist)
  print("A new list created from the Original list ",b)

#SPLICING - accesing parts
if 1:
 my_list = [1,2,3,4,5,6]
 print(my_list[0:len(my_list)])
 # OUTPUT [1, 2, 3, 4, 5, 6]
#Positional and Keyword arguments
if 0: 
 def fun(a,b,c):
    print(a,b,c)

 fun(1,2,3)  #Positional - here 1 will go in a ,2 in b and 3 in c

 fun(a=1,c=3,b=2) #Keyword - here order doesnt matter we explicitly denote which 
#                           argument goes in which parameter

#Default argumment - gives SyntaxError if non-defaults follow a default argument
if 0:
  def print_name(name = "No_name"):
    print(f"The name is {name}")

  print_name() 

# Variable length argument -In Python, variable-length arguments 
#                           let you pass any number of arguments to a function.
#                           using *var for positional arguments -> maintained as a list
#                           using **var for keyword arguments -> maintained as a dictionary
if 0:
 def fun(a,b,*args,**kwargs):
  print(f"The fixed arguments a = {a} and b = {b}")
  print("The positional varible length arguments maintained as list")
  print(args)
  print("The keyword varible length arguments maintained as dictionary")
  for key, value in kwargs.items():
    print(f"Argument name : {key} -> Argument value : {value}")  

 fun(1,2,3,4,name="adi",age=21)  # The function call only expects the two fixed 
 #                                 arguments a and b i.e wont give error if u give 
 #                                 only those two ,additional positional and keyword argSs 
 #                                 are optional (as syntax)        
 
 
 #Forcing keyword argument 
def funct(a,b,*,d,e):
  print(f"The normal non-default arguments a = {a},b = {b}")
  print(f"The enforced keyword arguments d = {d}, e = {e}")
funct(1,2,d="Ade",e="21") 

# Unpacking list,tuple,set (things without key-value pairs)
def fun(a,b,c):
  print(a,b,c)

my_list = [1,2,3] #The number of list elements should be equal to number of arg of fun
fun(*my_list)     #using a *my_list will put list items into a,b,c repective to order

# GIVES ERROR - my_list = [1,2,3,4] as fun() takes only 3 arguments a,b,c
# the above works same for tuple,set,any datatype not with key-value pairs

#Unpacking dictionary into arguments of a function
def fun(name,age,roll_No):
  print(name,age,roll_No)

my_dict = {"name" : "Adeeb","age" : 21, "roll_No" : 230301}
fun(**my_dict)

# WE USE ** IN CASE OF DICTS ,ALSO THE KEY NAMES AND NUMBER SHOULD MATCH TO THE 
# FUNCTION ARGUMENT NAMES AND NUMBER

# LOCAL VS GLOBAL VARIABLE
def fun():
  number = 3  #this number is local to the function only 

number = 0
fun()
print(f"The Global variable number {number}") #OUTPUT : 0

def fun():
  global number #this makes the local "number" variable the global "number" 
  number = 3

number = 0
fun()
print(f"The Global variable number {number}") #OUTPUT : 3

# PARAMETER PASSING - Call by object (call by object) and Call
#                     by object reference(call by reference)

# the immutable data type wont reflect any change made inside the local scope of a 
# function where the mutabble ones will



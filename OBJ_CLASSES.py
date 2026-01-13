# ALL METHODS IN THE CLASS MUST HAVE A self ARGUMENT - TO MAKE METHODS WITHOUT self 
# as an argument 
#EX 1
class student:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
    def show(self):
        for key,value in self.kwargs.items():
           print(f"{key} - {value}")

obj = student(name="adeeb",roll_no = 230301,Branch = "CSE")
obj.show()

#EX 2
class Student :
 collage_name = "mehh collage" # class atrribute - same for all objects here students
 #                             #                   occupies only 1 space 
 def __init__(self,name):        
    self.name = name           #object attribute - different for each object (denoted by .self)

student1 = Student("adeeb")
print(student1.name) #OUTPUT: adeeb
print(Student.collage_name) #OUTPUT: mehh collage 

#EX 3 - Methods in classes
class student:
   collage_name = "mehh collage"

   def __init__(self,name,roll_no):
      self.name = name
      self.roll_no = roll_no

   def show_name(self,message):
      print(f"The name of the student is {self.name}")  #self.name - means the name obj attribute
      print(f"An input of the show_name() - {message}")
   
   def show_rollNO(self):
      print(f"The name of the student is {self.roll_no}")

student1 = student("adeeb",230301)
student1.show_name("Hello there")
student1.show_rollNO()

#Ex 4
# Create a student class that takes name and marks of three subjects in the constructor
# and has a methof to print the average of those marks

class STUDENT:
   def __init__(self,name,my_dict):
      self.name = name
      self.my_dict = my_dict
      self.marks_list = list(my_dict.values())

   def show_avg(self):
      total = 0
      for marks in self.marks_list:
            total += marks
      average = total/3
      print(f"{self.name} has average marks - {round(average,2)}")

my_marks_dict = {} 
name = input("Enter student name: ")
i=1
while(i<4):
    sub_name = input(f"Enter the name of subject {i}:")
    marks = int(input(f"Enter marks obtained in {sub_name}: "))
    my_marks_dict[sub_name] = marks
    i = i + 1

student1 = STUDENT(name, my_marks_dict)
student1.show_avg()

# EX - 5 
# we have seen "self" now what is "cls" - this is used to refer the class attribute 
# but inorder to use this we need to decorate a method by "@class mathod"

class Student:
   clg_name = "ABC - collage"

   def __init__(self,name,roll_No):
      self.name = name
      self.roll_No = roll_No
    
   @classmethod
   def Change_collage(cls,new_clg):
      cls.clg_name = new_clg

student1 = Student("adeeb",230301)
print(Student.clg_name)

Student.Change_collage("xyz - collage")   # this change clg_name form "ABC - collage" to
#                                         # "xyz - collage"
print(Student.clg_name)

#Ex - 6
#static method - to create methods in the class which do not require a "self"
class A:
    @staticmethod
    def show():
        print("hi")  #This just print "hi" - doesnt require self

a = A()
a.show()

# we cand do the same by - manual way using staticmethod()
class A:
    def show():
        print("hi")  #This just print "hi" - doesnt require self
    show = staticmethod(show)    

a = A()
a.show()

#EX 7 - use del to delete objects and properies of abj like del a ,del a.show 

#Ex 8
# PYTHON has a bullshit private specifier - i.e it isnt a true private specifier just
# internla name changing an convention

class A:
   @staticmethod
   def __show():  #The "__" before show is making the show() private-like
      print("hello")

a = A()
a.__show()   # OUTPUT: 'A' object has no attribute '__show'
a._A__show() # OUTPUT: hello

#internally the "__" before show() changed its name from __show()
#to _A__show()

#EX-9
# acessing these private-like BS

class A:
   def __show():  #The "__" before show is making the show() private-like
      print("hello")

   def acess__show(self):
      self.__show()   # the "hello" output is due to this

a = A()
a.acess__show() #OUTPUT : hello 

#EX-10
# inheritance (example in custom exception)
# class car:
#  //some code
#
# class toyota_car(car)  #this class inherits methods and var of the parent class here "car"
#  //some code
 
#EX 11 
# @property - is a decorator which can be used on any method in the class to use the method
#             as a property/attribute/variable

#WITHOUT USING @property
class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_grade(self):
        if self.marks >= 50:
            return "Pass"
        return "Fail"

s = Student(65)
print(s.get_grade())   # OUTPUT-PASS

# Here inorder to get the grade of the student we need to make a function call 
# [s.get_grade()]

#USING @property
class Student:
    def __init__(self, marks):
        self.marks = marks

    @property
    def grade(self):
        if self.marks >= 50:
            return "Pass"
        return "Fail"

s = Student(65)
print(s.grade)   # OUTPUT-Pass

#Here inorder to get the grade of the student we dont need to make a function at all 
#we access the grade function as a varible due to the @property decorator 

#OPERATOR OVERLOADING - done using dunder functions (dunder literally means double 
# underscore eg __init__) 

class complex_num:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        new_real = self.real + other.real
        new_img = self.img + other.img
        return complex_num(new_real, new_img)

    def show_num(self):
        print(f"{self.real} + {self.img}i")

c1 = complex_num(1, 1)
c2 = complex_num(2, 3)
c3 = c1 + c2
c3.show_num()

# we dont call the dunder function directly ,Python calls them automatically when you 
# use built in operations (eg above)

#EX - 13
# Create an order class which stores the item and its price, Use the
# dunder function __gt__() to convey that 
# order1 > order2 if price of order1 > price of order two

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,other):
        if(self.price > other.price):
            return True 
        else :
            return False

order1 = order("shoes",190)
order2 = order("shirt",100)

if(order1 > order2):
    print(f"{order1.item} is more expensive then {order2.item}")
else :
    print(f"{order2.item} is more expensive then {order1.item}")    

      



      

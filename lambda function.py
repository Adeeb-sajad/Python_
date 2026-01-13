#lambda - is an anonymous(unanmed) one line function used in higher order functions(mainly),
#         a higher order function is a function that takes other functions as input
#         eg ,sorted(), map(), filer(), groupby()
#         this lambda function is written in the key argument of these functions

# Simple example 
add = lambda x, y :x + y
#    this is same as
def add(x, y):
    return x,y

# USE CASES - IN HIGHER ORDER FUNCTIONS


#                                #1 sorted()
if 0:
# Ex1 : Sort by y 
 Points_2D = [(1,2),(3,-6),(2,8),(5,0),(4,-1)]
 print(f"Unsorted points {Points_2D }") 
 Sorted_Points_2D = sorted(Points_2D) 
#By default the sorted function will sort according to the first argument
#here the 1 of (1,2), the 3 of (3,-6) and so on now if we wanna sort using
#the second argument i.e the 2 of (1,2),the -6 of (3,-6) <-.
 print(f"Sorted points {Sorted_Points_2D}")  #             |
# for this we use the second argument of sorted "key="   <-'

 Sorted_Points_2D_by_2nd_arg = sorted(Points_2D,key=lambda x:x[1])
 print(f"Sorted Points 2D by 2nd argument {Sorted_Points_2D_by_2nd_arg}")
# Here the lambda function takes the list as input and returns only the 

# Ex2 : Sort by sum of x and y 
if 0:
 Points_2D = [(1,2),(2,-6),(2,8),(5,0),(5,-1)]
 print(f"Unsorted points {Points_2D}")
 Points_2D = sorted(Points_2D,key= lambda x:x[0] + x[1])
 print(f"Sorted points [according to sum of x and y] {Points_2D}")
 #OUTPUT: [(2, -6), (1, 2), (5, -1), (5, 0), (2, 8)]
 #            |        |       |        |       |
 #            V        V       V        V       V
 #           -4        3       4        5       6

 #With reverse=True as argument ,this makes the sorting in descending order
  #OUTPUT: [(2, 8), (5, 0), (5, -1), (1, 2), (2, -6)]
 #            |        |       |        |       |
 #            V        V       V        V       V
 #            6        5       4        3      -4


#                              #2 map()
# changes element of any data structure according to a function which it takes as input

A = [1,2,3,4,5]
A = map(lambda x:x*x, A)
print(f"Squaring each element using map() {list(A)}")

# We can achieve the same effect using comprehension
A = [1,2,3,4,5]
A = [x*x for x in A]
print("Squaring each element using comprehension",A)

#                              #3 filter()
# similar in structure to the map() but returns only those elements for which the
# argument is true

A = [1,2,3,4,5]
A = filter(lambda x:x>3, A)
print(f"Using filter() to only get elements greater the 3 -> {list(A)}")
# OUTPUT : [4,5]

# We can achieve the same effect using comprehension
A = [1,2,3,4,5]
A = [x for x in A if x>2]
print("Using filter() to only get elements greater the 3 ->", A)


#                          #4 reduce()
# similar in structure to map() here the function applies to all elements and returns
# a single value EG sum of all elements in the list

from functools import reduce
A = [1,2,3,4,5]
SUM = reduce(lambda x,y:x+y, A)
print(f"Sum of all elements using reduce():{SUM}")



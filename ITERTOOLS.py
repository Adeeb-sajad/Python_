#ITERTOOLS - is a standard Python module that provides
#fast, memory-efficient tools for working with iterators (loops, combinations, permutations, etc)
# here - count, repeat, cycle are infinite iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, repeat, cycle
import operator

#product - gives the cartisian product
A = [1,2]
B = [3,4]
prod = product(A,B)
print(f"The cartisian product of AxB is {list(prod)}")
print("")

#permutations - arrangment where the order matters unlike combinations
A = [1,2,3]
per = permutations(A,3) # or permutations(A)
print(f"The permuatations of A are {list(per)}") 
print("")

#combinations - arrangment where the order doesnt matters
A = [1,2,3]
com = combinations(A,3)#here as ordeer doesnt matter 1,2,3 will have only one combination of 3
print(f"The combinations of A are {list(com)}") 
print("")

# we also have combinations_with_replacement - eg if A = [1,2,3] the combinations(A,2)
# will give (1,2),(2,1) and so on but wont give (1,1) , (2,2) but the 
# combinations_with_replacment will

#accumulate - used for accumulating the data/list
A = [1,2,3,4]
add_acc = accumulate(A)
print(f"A =",A)
print("Acumulated A using additions =",list(add_acc))
print("")

#We can also accumulate using multiplication but for that we need to import operations

mul_acc = accumulate(A, func = operator.mul)
print(f"A =",A)
print("  Acumulated A using multiplication =",list(mul_acc))
print("")

#groupby - groups the data/list based on a key(which is a function we define)
def smaller_then_3(x):
    return x<3

A = [1,2,3,4]
grp = groupby(A, key=smaller_then_3) #we grp the elements in A based on the smaller_then_3
#                                    #function
for key, value in grp:
    print(key,list(value))

print("")    

#OUTPUT
# True [1, 2]
# False [3, 4]

#Infinite iterators
 #count() - starts counting from a starting value given as an argument and also u can give steps
 #          default for steps is 1  
if 0:
 for i in count(1):
  print(i)

 #repeat() - simply repeats the given argument infinitely by default ,a second argument as
 #           number of times can also be given 
if 0:
 for i in repeat("a"):
  print(i)

 #cycle() - cycles through an iterable(list,str etc)
 #          infinitely (by defaulta second argument as
 #          number of times can also be given) i.e it goes one element at a time 
if 0:
 A = "hello"
 for i in cycle(A): 
   print(i)

from collections import Counter, namedtuple, defaultdict, deque

# Counter - counts how many times each element appears 
if 0:
 my_str = "adeeb"              # OUTPUT: 
 count = Counter(my_str)       # adeeb
 print(my_str)                 # Counter({'e': 2, 'a': 1, 'd': 1, 'b': 1})
 print(count)                  # [('e', 2)] - list given by count.most_common(1)
 #count.most_common(1)[0] - gives the first element of the list - ('e',2)
 #count.most_common(1)[0][0] - gives the first element of the tuple - 'e' 
 print("The most common char in my_str is",count.most_common(1)[0][0])

# namedtuple - lightwieght alternative to classes
if 0:
 Point = namedtuple('Point',"x,y,z")
 a = Point(0,1,2)              # OUTPUT: 
 print(a)                      # Point(x=0, y=1, z=2)
 print(f"x = {a.x}, y = {a.y}, z = {a.z}") # x = 0, y = 1, z = 2 (here we used string formating using the f-string)

# OrderedDict - early python version's the built in dict didnt remember aorder of insertion of elements 
#                but in newer version the OrderedDict is same as the built in dictionary data structure

# defaultdict - just like a normal dictionary but avoids KeyError as if we try to acess any key
#               value not in the dict it returns a defualt value of the data type set by us
if 0:
 my_dict = defaultdict(int)
 my_dict['a'] = 1
 my_dict['b'] = "2"

 for key , value in my_dict.items():
  print(f"Key({key}) -> Value({value})")

#Lets say we try to access a key "c which isnt ther in the defaultdict
 print(f"Not in the defaultdict - Value({my_dict["c"]})")   # OUTPUT - Value(0)
# as we gave my_dict = defaultdict(int) here int and default of int is 0

#deque - a double ended queue
if 0:
 d = deque()
 d.append(1)
 d.append(2)
# [(1,2)]
 d.appendleft(3)
# [(3,1,2)]
 d.extend([4,5,6]) # we have extendleft()
 print(d)         #OUTPUT - [(3,1,2,4,5,6)]

#Similarly we have methods like pop(),popleft(),clear()

 print(d)
 d.rotate(1)
 print("Rotated by 1",d) #Moves all elements 1 step to the right ,we can give -1
#                         rotates elements 1 step to the left



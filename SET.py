#SET - unordered ,immutable ,collection of unique elements 

#SYNTAX
myset = {1,2,3,2} 
print(myset)  #OUTPUT : {1,2,3} not {1,2,3,2} -> as 2 is repeated

nullset = set()
print(nullset)

#TRICK TO FIND HOW MANY UNIQUE CHARACTER DOES A STRING/WORD HAS
word = input("Enter the word/string:")
a_set = set(word)   # [INPUT:adeeb] in set it gets stored as a_set = {d,e,e,a,b}
print(len(a_set))   # But as duplicates are ignored in the set therefore [OUTPUT:4]

#frozenset - makes a set that is immutable
a = frozenset({1,2,3,4})
print(type(a))
a.add(9)
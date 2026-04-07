# 1) CONCEPT ABOUT PYTHON OBJECTS
#    1a) Python creates an integer object 10, and both a and b point to it
#        a ──► 10
#        b ──► 10
#        👉 There is one integer object 10 in memory
#        👉 Both variables reference it

#    1b) Python reuses small integers (typically from -5 to 256)
#        👉 This is called integer interning
#        So:
#          a = 10
#          b = 10
#        ✔ Python reuses the same object

#    1c) But this is NOT always guaranteed ,for 
#        large integer values lets say 1000 
#        Sometimes:
#           Same IDs (due to optimization)
#           Sometimes different

a = 10
b = 10

print(f"a id: {id(a)}")
print(f"b id: {id(b)}")

# 2) is operator - It checks: 
#                   “Do both variables point to the same object in memory?”
#                  Returns true if they do
#                  IN SHORT -> return true if address is same 

a = 1000
b = 1000

print(a == b)  # True
print(a is b)  # ??? 

# 👉 == → always True
# 👉 is → may be False



# 3) ABOUT COPY IN PYTHON
#    3a) What is a Copy in Python?
#        When you “copy” something, you’re trying to create another variable
#        that doesn’t mess with the original
#            COPY - A copy means creating a new object based on another object
#                   Goal:
#                        You want another variable
#                        That doesn’t unintentionally affect the original
#   3b) The opposite of copying is:
#       Reference (aliasing) — just another name for the same object
#             eg: B = [1, 2]
#                 A = B
#                    A ──┐
#                        ├──► [1, 2]
#                    B ──┘                
#                 👉 One object, two names



# 4) Types of copy in python 
#    4a) Shallow Copy - A shallow copy creates a new outer object,
#                       but inner objects are shared

#    EXAMPLE
A = [[1, 2], [3, 4]]
B = A.copy()

#    IN MEMORY
#       A ──► [L1, L2]
#       B ──► [L1, L2]   (new list, SAME inner lists)

# --Modify inner object-- #
A[0][0] = 999

print(A)
print(B)

# [[999, 2], [3, 4]]
# [[999, 2], [3, 4]]
# 👉 Both changed

# --Modify outer object-- #
A[0] = [100, 200]

print(A)
print(B)

# [[100, 200], [3, 4]]
# [[999, 2], [3, 4]]
#👉 Only A changed

#    4b) Deep copy - A deep copy creates a completely independent copy,
#                    including all nested objects
#    EXAMPLE
import copy

A = [[1, 2], [3, 4]]
B = copy.deepcopy(A)

#    IN MEMORY 
#       A ──► [L1, L2]
#       B ──► [L3, L4]   (new list, new inner lists)

# --Modify inner object--
A[0][0] = 999

print(A)
print(B)

# [[999, 2], [3, 4]]
# [[1, 2], [3, 4]]
# Both uneffected



# 5) COMMON CONFUSION

# Example with simple list
A = [1, 2, 3]
B = A.copy()

A[0] = 100
print(B)
# [1, 2, 3] - change not reflected

# Why no issue?
#   A)Integers are immutable
#     - What happens here is a shallow copy is created using the .copy() 
#       but it behaves as a deep copy now this happens because 
#       "Integers are immutable" But what does this actually mean 
#          IN MEMORY 
#            A ──► [ref→1, ref→2, ref→3]
#            B ──► [ref→1, ref→2, ref→3]
#          👉 Both lists share the same integer objects i.e
#          In simple words A[0] (which is 1) and B[0] point 
#          to the same integer object 1
#          NOW,
#            The question is what does this line do 
#              A[0] = 100
#            it does 2 seperate things 
#              a) Create new integer - 100  (new object created)
#              b) Change reference in list - 
#                  A ──► [ref→100, ref→2, ref→3]
#                  B ──► [ref→1,   ref→2, ref→3]
#                  👉 Only the pointer inside A changed
#              NOW,
#              Why B does NOT change
#                Because:
#                  B[0] still points to the old object 1
#                  That object was never modified 

# ALTHOUGH IN THE ABOVE EXAMPLE NO MUTATION WAS DONE ONLY REASSIGNMENT BUT 
# WE GIVE IMMUTABILITY AS REASON BECAUSE 
# In shallow copy, problems ONLY appear when mutation is possible
#  And:
#   Mutation is only possible with mutable objects



#  B)So it behaves like deep copy


# But with nested list 
A = [[1, 2]]
B = A.copy()

A[0][0] = 999
print(B)
# [[999, 2]]
# 👉 Now shallow copy problem appears



# 6) Reassignment and mutation 
#   6A) Reassignment - making a variable (or list slot) point to a NEW object
#                       eg: 
#                         A = [1, 2, 3]
#                         A[0] = 100
#                         What happens:
#                           Python creates a new object 100
#                           Changes what A[0] points to
#                         Memory:
#                           Before:
#                             A ──► [ref→1, ref→2, ref→3]
#                           After:
#                             A ──► [ref→100, ref→2, ref→3]
#                           👉 The integer 1 is untouched
#                           👉 Only the reference changed
#   Reassignment changes where the pointer points, not the object itself
#   
#   6B) Mutation - changing the object itself without changing its reference\\
#                  eg
#                    A = [[1, 2], [3, 4]]   
#                    A[0][0] = 999
#                    What happens:
#                      Python goes inside the inner list
#                      Modifies the value
#                    Memory:
#                     Before:
#                      L1 ──► [1, 2]
#                     After:
#                      L1 ──► [999, 2]
#                     👉 Same object (L1)
#                     👉 Content changed
#   Mutation changes data inside the object, not the reference   

# If you see = at an index → reference change (Reassignment)
# If you see [...][...] = → Mutation of inner object
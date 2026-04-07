A = [1, 20]
B = [i for i in A]

print("A id:", id(A))
print("B id:", id(B))

print("A[0] id:", id(A[0]))
print("B[0] id:", id(B[0]))

B[0] = B[0] + 10

print(" \n AFTER \n")

print("A id:", id(A))
print("B id:", id(B))

print("A[0] id:", id(A[0]))
print("B[0] id:", id(B[0]))

print("\n SEPERATE")
a = 10
b = 10

print(f"a id: {id(a)}")
print(f"b id: {id(b)}")

mystr = input("Enter: ")
mylist = mystr.split(" ")
print(f" {mylist} - {type(mylist)} ")
i = 0
ch = ""
while(i < len(mylist)):
    ch = ch + mylist[i][0]
    i = i + 1

print(f"The desired output is {ch}")
# dictionary - stores key value pairs, unordered, mutable ,Dont allow duplicates

if 0:
 my_dict = {"name":"adeeb","Age":23}
 print(my_dict)

 my_another_dict = dict(name="Adeeb",age=23)
 print(my_another_dict)

 A_dic = {
  "name": "Adeeb sajad",
  "cgpa": 8.8,
  "Age": 22,
  "Marks": [69,88,90]
 } 

 A_dic_Marks = A_dic["Marks"]
 print(type(A_dic_Marks))
 print(A_dic_Marks[0])
 print(A_dic["Marks"])

#Adding values
if 0: 
 my_dict = {"name":"adeeb","Age":23}
 my_dict["name"] = "sherich"
 print(my_dict)
 my_dict["section"] = "A"
 print(my_dict)

# NESTED-DICTIONARY
if 0:
 Products = {
  "The_eye":{
     "Pro1":{
      "Price":100,
       "Code":"A1"
    },
     "Pro2":{
      "Price":150,
      "Code":"A2"
    },
  },
  "Cosmos":{
     "Pro1":{
      "Price":180,
       "Code":"B1"
    },
     "Pro2":{
      "Price":950,
      "Code":"B2"
    },
  },
  "Sacred_geometry":{
     "Pro1":{
      "Price":70,
       "Code":"C1"
    },
     "Pro2":{
      "Price":1110,
      "Code":"C2"
    },
  }
 } 

 print("Price of Pro1 of Cosmos",Products["Cosmos"]["Pro1"]["Price"])
 print("Products and their discription of theme cosmos",Products["Cosmos"])

# .get() ka kamaal
if 0:
 my_dict = {"name":"adeeb","Age":23}
 print(my_dict.get("marks"))      # This gives [OUTPUT:None]
 print(my_dict.get("marks","Not present in the dictionary"))  #This gives [OUTPUT:Not present in the dictionary] 

#FUNCTIONS
if 0:
 my_dict = {"name":"adeeb","Age":23}
 lets_see = my_dict.keys()
 print(type(lets_see))
 print(lets_see)

 #other function are .values(), .item()

#To print or check if a value is present or not 
my_dict = {"name":"adeeb","Age":23}

#To check for something 

#a) for in loop
if "name" in my_dict:
 print("found")

#b) try except 
try:
 print(my_dict["name"])
except:
 print("error") 

#To print info from the dictionary
my_dict = {"name":"adeeb","Age":23}

#a)Prints the keys
for key in my_dict:
 print(key)

#b)Prints the values
for value in my_dict.values():
 print(value) 

#c)Prints key->value pairs
for key,value in my_dict.items():
 print(key,"->",value)
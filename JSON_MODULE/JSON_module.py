import json

#We have various function in this "json module"

#1) json.dumps() - which converts a python dict/python obj into a json_string
#                  (a string which will follow the javascript syntax)
if 0:
 python_dict = {
   "name":"adeeb",
   "age":21,
   "isStudent":True,
   "Backlogs":None
 }
#IN PYTHON - Boolean true is written as : True 
#IN JSON - Boolean true is written as : true

#IN PYTHON - null is written as : None
#IN JSON - null is writte as : null

 json_str = json.dumps(python_dict)

 print(f"The python dict/obj = {python_dict}")
 print("")
 print(f"The JSON string of the same dict using dumps() = {json_str}")

#2) json.loads() - which converts the json_string into a python dict/obj
if 0:
 json_str1 ='{"name": "adeeb", "age": 21, "isStudent": true, "Backlogs": null}'
 python_dict1 = json.loads(json_str1)

 print(f"The JSON string = {json_str1}")
 print("")
 print(f"The python dict/obj of the same json_str1 using loads() = {python_dict1}")

#3) json.load() - reads from the json file 
if 0:
 python_obj = {}
 with open(r"D:\CSE\python\JSON_MODULE\data.json","r") as f:
  python_obj = f.read()

 print(python_obj)
 
#4) json.dump() - write into the json file 
# New student to add
new_student = {
    "id": 7,
    "name": "sherich Youshush",
    "marks": 79
}

# Path to your JSON file
file_path = r"D:\CSE\python\JSON_MODULE\data.json"

# Step 1: Read existing JSON data
with open(file_path, "r") as f:
    data = json.load(f)  # data is a dict

# Step 2: Append new student to the 'students' list
data["students"].append(new_student)

# Step 3: Write updated data back to file
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

print("New student added successfully!")

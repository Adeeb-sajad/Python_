import json 

json_str1 ='{"name": "adeeb", "age": 21, "isStudent": true, "Backlogs": null}'
python_dict1 = json.loads(json_str1)

print(f"The JSON string = {json_str1}")
print("")
print(f"The python dict/obj of the same json_str1 using loads() = {python_dict1}")
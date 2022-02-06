import json


#1. Convert json string into a python object/dictionary

json_string = '{"first_name":"Thomas","last_name":"Meier","city":"Frankfurt"}'

json_data = json.loads(json_string)

print(json_data,type(json_data))
print(json_data['city'])

#####################################################
# 2. Convert Python dictionary to a JSON string
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = {"first_name":"Thomas","last_name":"Meier","city":"frankfurt"}

json_string = json.dumps(x)
print(json_string,type(json_string))
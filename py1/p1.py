import json

dict = {
    "emp1": {
        "name": "Lisa",
        "lastname": "Manoban"
    },
    "emp2": {
        "name": "Elis",
        "lastname": "Yovovich"
    },
}
json_format = json.dumps(dict, indent = 2, separators = ("-", ":"), sort_keys = True)
print(json_format)
#####################################
friends_list = ['John', 'Alexei', 'Sam',]
json_format = json.dumps(friends_list)
print(json_format)
#####################################
str = "abc"
json_format = json.dumps(str)
print(json_format)
##################################### load
print ()
f = open('data.json', )
data = json.load(f)

print(json.dumps(data, indent = 2, separators = ("-", ":"), sort_keys = True))
# Closing file
f.close()
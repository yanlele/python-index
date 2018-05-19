import json

numbers = [1,2,3,4,7,11,13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
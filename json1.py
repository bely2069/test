import json

file_name='not_valid_json.json'#path file
try:
    with open(file_name, 'r') as f:
        try:
            data = json.load(f)#load file
            print('Proper file ')
        except Exception as e:
            print('is not proper file '+e)
except :
    print('not found file')




import json
import time
file_name='not_valid_json.json'#path file
try:
    with open(file_name, 'r') as f:
        try:
            data = json.load(f)#load file
            print('Proper file ')
            time.sleep(5)
        except Exception as e:
            print('is not proper file '+e)
            time.sleep(5)
except :
    print('not found file')
    time.sleep(5)





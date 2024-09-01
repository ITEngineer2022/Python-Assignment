import sys
import json
import time
argList=sys.argv

with open('structure.json') as f:
    output_data = json.load(f)

# 1st task
if len(argList)==1:
    for data in output_data["contents"]:
        if not data["name"].startswith('.'):
            print(data["name"],end="   ")

# 2nd task
elif argList[1]=='-A':
    for data in output_data["contents"]:
        print(data["name"],end="   ")

#3rd task
elif argList[1]=='-l':
    for data in output_data["contents"]:
        if not data["name"].startswith('.'):
            print(data["permissions"],data['size'],time.strftime('%d %b %H:%M', time.gmtime(data['time_modified'])),data['name'])      

    

    

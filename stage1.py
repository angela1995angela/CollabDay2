import requests
import json
import fileinput

token = "N2U5ZTNiMjYtNjNkMy00MGYwLTg1MTYtN2MwZWJkMjFlYjA1N2NkMTk3Y2EtYjcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
base_url = 'https://webexapis.com/v1'
endpoint = '/rooms'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

room_body ={
    "title":"Test Room 1"
}


response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(room_body)).json()
     
roomid=response['id']
print(roomid)
# Read in the file
with open('env.py', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('<Replace me in stage 1>', roomid)

# Write the file out again
with open('env.py', 'w') as file:
    file.write(filedata)



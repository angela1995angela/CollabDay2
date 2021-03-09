import requests
import json
import fileinput

token = "N2U5ZTNiMjYtNjNkMy00MGYwLTg1MTYtN2MwZWJkMjFlYjA1N2NkMTk3Y2EtYjcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
base_url = 'https://webexapis.com/v1'
endpoint = '/rooms?type=group'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}


try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        get_rooms = response.json()
        rooms=get_rooms['items']
        for room in rooms:
            if room['title']=="Programmability CTF - Day 1 - Team 1":
                roomid=room['id']
                print(roomid)
    
    # Read in the file
    with open('env.py', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('<Replace me in stage 0>', roomid)

    # Write the file out again
    with open('env.py', 'w') as file:
        file.write(filedata)

                
except Exception as ex:
    print(ex)



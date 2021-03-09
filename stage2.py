import requests
import json

token = "N2U5ZTNiMjYtNjNkMy00MGYwLTg1MTYtN2MwZWJkMjFlYjA1N2NkMTk3Y2EtYjcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
base_url = 'https://webexapis.com/v1'
endpoint1 = '/meetings'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}


numOfMeetings=0
response = requests.get(url=f"{base_url}{endpoint1}", headers=headers).json()
for meeting in response['items']:
    numOfMeetings=numOfMeetings+1


endpoint2 = '/rooms?type=group'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

numOfSpaces=0
response = requests.get(url=f"{base_url}{endpoint2}", headers=headers).json()
for space in response['items']:
    numOfSpaces=numOfSpaces+1


endpoint3 = '/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vOTI1MTg2NTAtODBiZS0xMWViLWIyYzctOGQ4MTk0OWE4MmU3'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

numOfMessages=0
response = requests.get(url=f"{base_url}{endpoint3}", headers=headers).json()
for msg in response['items']:
    numOfMessages=numOfMessages+1


endpoint4 = '/messages'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vOTI1MTg2NTAtODBiZS0xMWViLWIyYzctOGQ4MTk0OWE4MmU3",
    "text": f"Informative message: The total number of meetings that I have planned is: {numOfMeetings}. The total number of spaces that I am part of is: {numOfSpaces}. The total number of messages that I had sent in this space until now is: {numOfMessages}."
}

response = requests.post(url=f"{base_url}{endpoint4}", headers=headers, data=json.dumps(body)).json()

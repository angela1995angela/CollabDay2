import requests
import json

token = "N2U5ZTNiMjYtNjNkMy00MGYwLTg1MTYtN2MwZWJkMjFlYjA1N2NkMTk3Y2EtYjcx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
base_url = 'https://webexapis.com/v1'
endpoint = '/messages'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

body ={
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vOTI1MTg2NTAtODBiZS0xMWViLWIyYzctOGQ4MTk0OWE4MmU3",
    "text":"Hello!"
}

response = requests.post(url=f"{base_url}{endpoint}", headers=headers, data=json.dumps(body)).json()
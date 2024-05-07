import requests
import requests.auth

client_auth = requests.auth.HTTPBasicAuth('bshxZJtMB6WAuv2-bBu5JQ', 'Or_KbNd9DLY42ODQqgWjjlJi40K94g')
post_data = {"grant_type": "password", "username": "Mission-Afternoon425", "password": "Fy!thk!bz22"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}

response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

#url = 'https://www.reddit.com/api/v1/access_token?grant_type=client_credentials'

#token = requests.post(url, data= {'key': 'value'})

auth_0 = response.json()

print(auth_0)

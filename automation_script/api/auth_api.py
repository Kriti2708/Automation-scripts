import json
import requests
from pprint import pprint

base_url = "https://node-fake-api-server.herokuapp.com/user"
payload = {"external_id": "postman"}
headers = {'Content-Type': "application/json,text/plain",
           'X-FakeAPI-Action': 'register'
           }

response = requests.request('POST', url=base_url, data=payload, headers=headers)
data = response.json()
auth_token = data["auth_token"]
print("Authentication_Token :: ", auth_token)
username = data["username"]
print("Username :: ", username)
password = data["password"]
print("Password :: ", password)

print("Response Status Code :: ", response.status_code)
print("Response url :: ", response.url)
print("Response Headers :: ", response.headers)
print("Response Encoding :: ", response.encoding)
print("Response Elapse ::", response.elapsed)
print("Response Cookies :: ", response.cookies)
print("Response Request :: ", response.request)
print("Response History :: ", response.history)
print("Response Links :: ", response.links)
print("Response Reason ::", response.reason)
print("Response Raw ::", response.raw)
print("Response Text ::", response.text)

import requests

base_url = "http://calapi.inadiutorium.cz/api/v0/en/calendars/general-en/yesterday"
BODY = "formdata"

response = requests.request("Get", url=base_url, data=BODY)
data = response.json()

print("Response Status Code - ", response.status_code)
print("Response url - ", response.url)
print("Response Headers - ", response.headers)
print("Response Encoding - ", response.encoding)
print("Response Elapse - ", response.elapsed)
print("Response Cookies - ", response.cookies)
print("Response Request - ", response.request)
print("Response History - ", response.history)
print("Response Links - ", response.links)
print("Response Reason - ", response.reason)
print("Response Raw - ", response.raw)

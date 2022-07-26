import requests

base_url = "https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year=now&month=x&ss=on&mf=on&c=on" \
           "&geo=geoname&geonameid=3448439&m=50&s=on "
params = {"v": "1", "cfg": "json",
          "maj": "on", "min": "on",
          "mod": "on", "nx": "on",
          "year": "now", "month": "x",
          "ss": "on", "mf": "on",
          "c": "on", "geo": "geoname",
          "geonameid": "3448439", "m": "50",
          "s": "on"}

response = requests.request("Get", url=base_url, params=params)
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

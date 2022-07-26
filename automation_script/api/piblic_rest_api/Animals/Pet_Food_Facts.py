import requests

base_url = "https://world.openpetfoodfacts.org/api/v0/product/20106836.json"

response = requests.request('GET', url=base_url)
data = response.json()

print("Response URL - ", response.url)
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
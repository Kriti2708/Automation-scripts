from pprint import pprint
import requests


def locations():
    base_url = "https://ghibliapi.herokuapp.com/locations"
    response = requests.request("Get", url=base_url)
    print(response.content)
    # data = self.response.json()

# print("Response Status Code - ", response.status_code)
# print("Response url - ", response.url)
# print("Response Headers - ", response.headers)
# print("Response Encoding - ", response.encoding)
# print("Response Elapse - ", response.elapsed)
# print("Response Cookies - ", response.cookies)
# print("Response Request - ", response.request)
# print("Response History - ", response.history)
# print("Response Links - ", response.links)
# print("Response Reason - ", response.reason)
# print("Response Raw - ", response.raw)

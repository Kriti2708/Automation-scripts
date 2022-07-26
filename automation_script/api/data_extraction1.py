import json
import numpy as np

import requests

base_url = 'https://www.anapioficeandfire.com/api/characters'

response = requests.request("GET", url=base_url)

print("Response Url - ", response.url)
print("Response content - ", response.content)
print("Response text - ", response.text)
print("Response headers - ", response.headers)

data = response.json()
data_extract = np.array(data)
print('Format in Array from with Numpy :: ', data_extract)

data1 = response.json()

url1 = data1[0]['url']
print('url 1 is :: ', url1)
gender1 = data1[0]['gender']
print('gender1 is :: ', gender1)
culture1 = data1[0]['culture']
print('culture1 is :: ', culture1)

url2 = data1[1]['url']
print('url 2 is :: ', url2)
gender2 = data1[1]['gender']
print('gender2 is :: ', gender2)

tvseries_season1 = data1[1]['tvSeries'][0]
print('tvseries_season 1 is :: ', tvseries_season1)

playedBy = data1[1]['playedBy'][0]
print('Played By is :: ', playedBy)

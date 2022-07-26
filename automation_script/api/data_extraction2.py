import numpy as np
import requests

base_url = 'https://www.anapioficeandfire.com/api/books'

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
print("This is the URL 1- ", url1)

name1 = data1[0]['name']
print("This is name 1 - ", name1)

isbn1 = data1[0]['isbn']
print("this is isbn - ", isbn1)

char1 = data1[0]["characters"][0]
print("This is Characters - ", char1)

pov_char5 = data1[5]['povCharacters'][0]
print("This is pov character", pov_char5)

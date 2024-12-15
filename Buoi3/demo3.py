import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Python'
headers = requests.utils.default_headers()
r = requests.get(url, headers)

bs = BeautifulSoup(r.content, 'html.parser')
images = bs.find_all('img')
print('total images:', len(images))
for i in images:
    print(i['src'])
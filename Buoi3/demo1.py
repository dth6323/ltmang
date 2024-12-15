#in api cua nhung website va gui query duoi nhung phuong thuc get
import requests
url = 'https://pixabay.com/en/photos/'

params ={'q':'tiger', 'order': 'popular','min_width':'800', 'min_height': '600'}

r = requests.get(url, params=params)
print(r.url)
#thi cuoi ki lay api, thuc hien get search

#chi lay ra nhung anh thoa man nhung tieu chi cua minh thoy

#download anh, image, text
import urllib.request
print('starting downloading....')
url = 'https://www.python.org/static/img/python-logo@2x.png'
#dia chi website muon download ve
urllib.request.urlretrieve(url,'python.png')
with urllib.request.urlopen(url) as r:
    print('status', r.status)
    print('starting downloading python.org')
    with open('python.org','wb') as image:
        image.write(r.read())

#post: day thong tin len server

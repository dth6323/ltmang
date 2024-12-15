import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
#lay ra tat ca cac link cua trang web
# url = urlopen('https://en.wikipedia.org/wiki/Python') 
# bs = BeautifulSoup(url)
# for link in bs.find_all("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
        
#tim xem co bao nhieu anh trong web site, in ra link anh(cau hoi trong de thi lay ra cac file)
# url = urlopen('https://en.wikipedia.org/wiki/Python') 
# bs = BeautifulSoup(url)
# for link in bs.find_all('img'):
#     if 'src' in link.attrs:
#         print(link.attrs['src'])

#dung thu vien request dem anh va in ra co bao nhieu link anh
# Replace with the URL of the website you want to scrape
url = 'https://en.wikipedia.org/wiki/Python'

# Fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags
    images = soup.find_all('img')

    # Extract the source URLs of the images
    img_urls = [img['src'] for img in images if 'src' in img.attrs]

    # Print the image URLs
    for i, img_url in enumerate(img_urls, start=1):
        print(f"Image {i}: {img_url}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

        
#bai tap lay thong tin ket qua so xo
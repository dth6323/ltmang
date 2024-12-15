import requests
from bs4 import BeautifulSoup
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
}
link="https://sis.utc.edu.vn"
url="https://sis.utc.edu.vn/survey/overview.php"
username="ha211240940@lms.utc.edu.vn"
password="Cnfp56q37n@sis"
data={
    "username":username,
    "password":password
}
response = requests.post(link,data=data,headers=header)

#lay thong tin cua khao sat
if response.status_code == 200:
    print("Dang nhap thanh cong")
    # soup = BeautifulSoup(response.text, 'html.parse')
else:
    print("Dang nhap ko thanh cong")
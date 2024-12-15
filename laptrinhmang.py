from urllib.request import urlopen
from urllib.request import Request
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import datetime

if __name__ == '__main__':
    # r = Request('http://www.gmail.com')
    # r = Request('http://www.python.org')
    # rl = urlopen(r)
    # print(r.url)
    # print(rl.url)

    # check xem truy cap bang trinh duyet nao
    # print(r.get_header('User-agent'))

    # in ra đường link redirect
    # print(r.redirect_dict)

    # in ra cookie
    cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj))
    r = opener.open('http://www.github.com')
    # print(r)
    # print(len(cj))

    cookies = list(cj)
    print(cookies)
    print(cookies[1].name)
    print(cookies[1].value)
    print(cookies[1].domain)
    print(cookies[1].path)
    print(datetime.datetime.fromtimestamp(cookies[1].expires))
    print(cookies[1].secure)

    # for cookie in cookies:
    #     print(cookie.name)
    #     print(cookie.value)
    #     print(cookie.domain)
    #     print(cookie.path)
    #     print(cookie.expires)
    #     print(cookie.secure)
    #     print('------------------')

    # trich ra tung phan cua url

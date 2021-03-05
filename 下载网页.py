import urllib.request
import requests

url = 'http://python.org'
print(urllib.request.urlopen(url).read())

if __name__ == '__main__':
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)

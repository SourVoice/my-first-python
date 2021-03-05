import urllib.request
from urllib import response

url = 'http://python.org'
ret = urllib.request.urlopen(url)
html = response.read()
print(html)

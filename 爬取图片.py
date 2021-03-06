from bs4 import BeautifulSoup
import urllib.request
import requests
import sys


def download_p(block_size, block_num, total_size):
    """
    :param block_size:
    :param block_num:
    :param total_size:
    :return:
    """
    sys.stdout.write("--已下载:%.2f%%" % float(block_size * block_num / total_size) * 100 + '\r')
    sys.stdout.flush()


if __name__ == '__main__':
    target = 'https://baijiahao.baidu.com/s?id=1662783963649610289&wfr=spider&for=pc'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    div = bf.find_all('div', class_='img-container')
    a = BeautifulSoup(str(div[0]), 'html.parser')
    a_div = a.find('img', class_='large')
    url = a_div.get('src')

    image_name = url.split('=')[-1]
    path = 'C:/Users/rockstar/Desktop/fiction/' + image_name
    urllib.request.urlretrieve(url, path, download_p)

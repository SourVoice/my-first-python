import requests
from bs4 import BeautifulSoup
import sys


class Download(object):
    def __init__(self):
        self.server = 'https://www.ncxsl.com/'
        self.target = 'https://www.ncxsl.com/book/2'
        self.nums = 0
        self.names = []
        self.urls = []

    def get_url(self):
        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        # <div class="mulu"><ul>
        div = bf.find_all('div', class_='mulu')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(each.get('href'))

    @staticmethod
    def get_content(target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        div = bf.find_all('div', class_="yd_text2")
        texts = div[0].text  # 这里的&emsp格式空格可以直接被编译
        return texts

    @staticmethod
    def writer_to(name, texts):
        with open('C:/users/rockstar/Desktop/fiction/girl_run_into_solider', 'a', encoding='UTF-8') as f:
            f.write(name + '\n')
            f.writelines(texts)
            f.write('\n\n')


if __name__ == '__main__':
    dl = Download()
    dl.get_url()
    for i in range(dl.nums):
        dl.writer_to(dl.names[i], dl.get_content(dl.urls[i]))
        sys.stdout.write(' 进度: %.3f%%' % float(i / dl.nums))
        sys.stdout.flush()
    print('下载完成')
# success

from bs4 import BeautifulSoup
import requests
import sys


class DownloadAim(object):
    def __init__(self):
        self.server = 'https://www.bqkan.com/'
        self.target = 'https://www.bqkan.com/1_1094/'
        self.urls = []  # 下载链接
        self.nums = 0  # 章节数目
        self.name = []  # 章节名称

    # 获取章节内容
    @staticmethod  # 改用静态方法,类函数不用在定义一个self
    def get_contents(target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        text = bf.find_all('div', class_='showtxt')
        text = text[0].text.replace('\xa0' * 8, '\n\n')
        return text

    # 获取下载链接
    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        for each in a[12:]:
            self.name.append(each.string)
            self.urls.append(self.server + each.get('href'))

    # 下载内容写入文档:
    @staticmethod  # 改用静态方法,类函数不用在定义一个self
    def write_to_text(name, text):
        with open('C:/Users/rockstar/Desktop/fiction/novel.txt', 'a', encoding='UTF-8') as f:  # 注意编码格式
            f.write(name + '\n')  # 章节名称
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = DownloadAim()
    dl.get_download_url()
    print('开始下载被爬小说:')
    for i in range(dl.nums):
        dl.write_to_text(dl.name[i], dl.get_contents(dl.urls[i]))
        sys.stdout.write("--已下载:%.3f%%" % float(i / dl.nums) + '\r')  # 这里要按回车才能显示出进度
        sys.stdout.flush()
    print('下载完毕')
# 缺点:stdout不能实时显示下载进度

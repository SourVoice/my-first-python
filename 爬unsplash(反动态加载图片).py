import requests
import urllib.request
import json
import time
import sys


# 动态加载网站


class Download(object):
    def __init__(self):
        self.serve = 'https://unsplash.com/napi/photos?per_page=12&page='
        self.headers = {
            'user - agent': 'Mozilla / 5.0'
        }
        self.urls = []  # 模拟滚动所得的地址,函数中定义了页数
        self.download_urls = []  # 解析json所得的图片下载地址,每页12张图
        self.image_name = []
        self.paths = []

    # 人工创造一个向下滚动的行为
    def create_link(self):
        for i in range(3, 4):
            self.urls.append(self.serve + str(i))

    def get_image_url(self, target):
        req = requests.get(target, self.headers)
        json_data = json.loads(req.text)  # 返回一个列表对象<class 'list'>  但列表中每一行为字典(for each in json_data)\
        # type(each): <class 'dict'>
        for each in json_data:
            if each['alt_description'] is not 'None':
                # print(each['alt_description'])
                # print('---------------------------------------------------------------------', '\n')
                self.image_name.append(each['alt_description'])  # 为图片命名
            elif each['description'] is not 'None':
                # print(each['description'])
                # print("---------------------------------------------------------------------", '\n')
                self.image_name.append(each['description'])  # 为图片命名
            self.download_urls.append(each['links']['download'])
            # print(each['links']['download'] + '\n')

    def write_in(self):
        for each in self.image_name:
            self.paths.append("C:/Users/rockstar/Desktop/fiction/image/" + str(each))
        for (each1, each2) in zip(self.download_urls, self.paths):
            urllib.request.urlretrieve(each1, each2 + '.jpg', self.download_p)
            time.sleep(1)

    @staticmethod
    def download_p(block_size, block_num, total_size):
        """
        :param block_size:
        :param block_num:
        :param total_size:
        :return:
        """
        sys.stdout.write("--已下载:%.1f%%" % float(block_size * block_num / total_size) * 100 + '\r')
        sys.stdout.flush()


if __name__ == '__main__':
    dl = Download()
    dl.create_link()  # 创造了7页
    for each in dl.urls:
        dl.get_image_url(each)
    dl.write_in()
# success!!

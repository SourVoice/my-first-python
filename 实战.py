import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 1.请求网站
    target = 'https://www.bqkan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    # 2.获取文本,查找属性标签
    html = req.text
    bf = BeautifulSoup(html, "html.parser")  # 解析html时指定解析器为html.parser
    # texts = bf.find_all('div', class_='showtxt')  # 获取classs属性为showtxt的<div>
    # print(texts[0].text.replace('\xa0' * 8, '\n\n'))  # 去掉<br>和空格(html中是&nbsp)
    # text能够提取文本,去除br标签
    # 第二个参数来去除第一个参数
    # 因为find_all返回列表,所以用texts[0]来承载返回元素

    # 3.查找父节点和子节点:<div>//</div>....,并匹配标签(从父标签开始)
    # 爬取目录
    target2 = "https://www.bqkan.com/1_1094/"
    req2 = requests.get(url=target2)
    html2 = req2.text.encode('iso-8859-1')  # 将html改为支持汉字的编码
    div_bf = BeautifulSoup(html2, "html.parser")
    div = div_bf.find_all('div', class_='listmain')
    # print(div[0].text)
    # 抓取<a>标签中的href(超链接)
    a_bf = BeautifulSoup(str(div[0]), 'html.parser')  # 不知到为什么这里也有解析警告??(我也另解析了一次)
    a = a_bf.find_all('a')
    server = 'http://bqkan.com'
    del a[0:12]  # 删除没用的前几行
    for each in a:  # each.string获取章名
        print(each.string, server + each.get('href'))  # each.get('herf')来获取属性值

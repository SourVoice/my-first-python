import os

filename = 'C:/Users/rockstar/Desktop/fiction/'
path = filename + 'text.txt'
url = 'https://www.python.org/'
# noinspection PyBroadException
# 去掉Exception单独使用的警告(上面一行)
try:  # 用os模块检查路径
    if not os.path.exists(filename):
        os.mkdir(filename)
    if not os.path.exists(path):
        url.raise_for_status()

    else:
        print("图片已存在")
except Exception as e:
    print("图片获取失败")

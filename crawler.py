# coding:utf-8
import requests  # 导入requests库
from bs4 import BeautifulSoup

r = requests.get('https://unsplash.com')  # 像目标url地址发送get请求，返回一个response对象
# print(r.text)  # r.text是http response的网页HTML

# 搜索标签
soup = BeautifulSoup(r.text, 'lxml')  # 声明BeautifulSoup对象
find = soup.find('p')  # 使用find方法查到第一个p标签
print("find's return type is ", type(find))  # 输出返回值类型
print("find's content is", find)  # 输出find获取的值
print("find's Tag Name is ", find.name)  # 输出标签的名字
print("find's Attribute(class) is ", find['class'])  # 输出标签的class属性值
print('NavigableString is：', find.string)
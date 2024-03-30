import requests
from bs4 import BeautifulSoup
import re

def get_scholarship_info(url,name,date,keyword='奖学金'):
    response = requests.get(url)
    response.encoding = 'utf-8'  # 设置编码
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有的<li>元素
    li_elements = soup.find_all('li')
    dd_elements = soup.find_all('dd')
    # 定义日期的正则表达式
# 定义日期的正则表达式
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    print(name + '奖学金信息：')
    # 检查每个<li>元素的文本内容是否包含日期
    if date:
        for li in li_elements:
            if keyword in li.text and date_pattern.search(li.text):
                print(li.text)
    else:
        for li in li_elements:
            if keyword in li.text:
                print(li.text)
    if date:
        for dd in dd_elements:
            if keyword in dd.text and date_pattern.search(dd.text):
                print(dd.text)
    else:
        for dd in dd_elements:
            if keyword in dd.text:
                print(dd.text)

# 使用你的URL
get_scholarship_info('https://me.bit.edu.cn/rcpy/xsgztz/index.htm','机械工程学院',True)

get_scholarship_info('https://sie.bit.edu.cn/tzgg/zhtz/index.htm','信息与电子学院',False)

get_scholarship_info('https://smen.bit.edu.cn/tzgg/','机电学院',True)

get_scholarship_info('https://sae.bit.edu.cn/tzgggb/','宇航学院',True)

get_scholarship_info('https://sme.bit.edu.cn/tzgg/','材料学院',True)

get_scholarship_info('https://ac.bit.edu.cn/tzgg/','自动化',True)

get_scholarship_info('https://cs.bit.edu.cn/tzgg/','计算机',False)

get_scholarship_info('https://arims.bit.edu.cn/tz/','前沿交叉',True)

get_scholarship_info('https://opt.bit.edu.cn/tzgg2/tzgg/','光电学院',False)

input("按任意键退出...")
import requests
from bs4 import BeautifulSoup 
import re
import json

def get_scholarship_info(url,name,flag,keyword='学金'):
    response = requests.get(url)
    response.encoding = 'utf-8'  # 设置编码
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有的<li>元素
    li_elements = soup.find_all('li')
    dd_elements = soup.find_all('dd')
    # 定义日期的正则表达式
    # 定义日期的正则表达式
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    scholarship_info = {}

    print('**********'+name + '奖学金信息：' + '**********')
    # 检查每个<li>元素的文本内容是否包含日期
    if flag:
        for li in li_elements:
            if keyword in li.text and date_pattern.search(li.text):
                print('{:<50}'.format(li.text.replace('\n', '')))

                date = date_pattern.search(li.text).group()
                scholarship_info[date] = {'name': name, 'info': li.text.replace('\n', '')}

        for dd in dd_elements:
            if keyword in dd.text and date_pattern.search(dd.text):
                print('{:<50}'.format(dd.text.replace('\n', '')))

                date = date_pattern.search(dd.text).group()
                scholarship_info[date] = {'name': name, 'info': dd.text.replace('\n', '')}
    else:
        for li in li_elements:
            if keyword in li.text:
                print('{:<50}'.format(li.text.replace('\n', '')))

                scholarship_info['no_date'] = {'name': name, 'info': li.text.replace('\n', '')}
        for dd in dd_elements:
            if keyword in dd.text:
                print('{:<50}'.format(dd.text.replace('\n', '')))

                scholarship_info['no_date'] = {'name': name, 'info': dd.text.replace('\n', '')}
    print('\n')

##Main函数
with open('website.json', 'r',encoding = 'utf-8') as f:
    websites = json.load(f)
# 遍历列表，对每个网站调用 get_scholarship_info 函数
all_scholarships = []
# 遍历列表，对每个网站调用 get_scholarship_info 函数
for website in websites:
    all_scholarships.append(get_scholarship_info(website['url'], website['name'], website['flag']))

with open('scholarships.json', 'w', encoding='utf-8') as f:
    json.dump(all_scholarships, f, ensure_ascii=False)

input("按任意键退出...")
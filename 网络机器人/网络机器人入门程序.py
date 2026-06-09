import requests
from lxml import html
# 定义url
target_url ="https://www.tiobe.com/tiobe-index/"

# 发送get请求
response = requests.get(target_url)

document = html.fromstring(response.text)

# 解析表头
th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格中的数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)

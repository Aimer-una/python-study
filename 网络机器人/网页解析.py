from lxml import html

# 读取html文件
with open("resources/仙逆人物志.html","r",encoding="utf-8") as f:
    html_doc = f.read()

    # 解析html的文本，将其转换成一个文档对象
    document = html.fromstring(html_doc)

    # 解析表头 -xpath语法
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)

    # 获取所有行数据
    tr_list = document.xpath("//table/tbody/tr")
    for tr in tr_list:
        # 获取行数据
        td_list = tr.xpath("./td/text()")
        print(td_list)
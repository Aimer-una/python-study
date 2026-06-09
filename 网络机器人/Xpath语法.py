from lxml import html

# 读取html文件
with open("resources/仙逆人物志.html","r",encoding="utf-8") as f:
    html_doc = f.read()

    # 解析html的文本，将其转换成一个文档对象
    document = html.fromstring(html_doc)

    # 匹配class属性为p的标签
    p_list = document.xpath("//p[@class]/text()")
    print(p_list)

    # *：匹配任意标签
    th_list = document.xpath("//thead/tr/*/text()")
    print(th_list)

    a_list = document.xpath("//td/img/@*")
    print(a_list)
import json

# 写入json文件

user = {
    'name': '张润',
    'age': 18,
    'hobby': ['看电影', '看小说'],
    'gender': '女'
}
with open('resources/user.json', 'w', encoding='utf-8') as f:
    # ensure_ascii: 默认为True，确保输出为ascii编码(非ascii会进行转义);False,非ascii码保留原样输出
    # indent: 缩进
    json.dump(user, f, ensure_ascii=False, indent=2)


# 读取json文件
with open('resources/user.json', 'r', encoding='utf-8') as f:
    user = json.load(f)
    print(user)
    print(type(user))
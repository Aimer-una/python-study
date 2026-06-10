import re

s1 = "13876088476是我的电话号码"
s2 = "我的电话号码是13876088476 另一个电话号码是13876086310 QQ号是12345 另一个QQ号是197511012123"

# match - 从字符串的开头开始匹配（匹配第一个匹配项）---Match对象
result = re.match(r"1[3-9]\d{9}",s1)
print(result)
print(result.group()) # 匹配结果
print(result.span()) # 开始位置和结束位置
print(result.start()) # 开始位置
print(result.end()) # 结束位置
print("==============================================================")
# search - 从字符串的任意位置开始匹配（匹配第一个匹配项）---Match对象
result = re.search(r"1[3-9]\d{9}",s2)
print(result.group()) # 匹配结果
print(result.span()) # 开始位置和结束位置
print(result.start()) # 开始位置
print(result.end()) # 结束位置

print("==============================================================")
# findall - 从字符串中匹配所有结果（返回所有匹配项）---list
result = re.findall(r"1[3-9]\d{9}",s2)
print(result)

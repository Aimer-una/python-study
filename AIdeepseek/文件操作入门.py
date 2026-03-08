# 读文件
# 打开文件
f = open('resources/A-SOUL.txt', 'r', encoding='utf-8')

# 读取文件
content = f.read()
print(content)

# 关闭文件流
f.close()

# 写文件
# 创建文件
f = open('resources/静夜思.txt', 'w', encoding='utf-8')

# 写入文件内容
f.write('静夜思\n \n')
f.write('窗前明月光，\n')
f.write('疑是地上霜. \n')
f.write('举头望明月，\n')
f.write('低头思故乡. \n')

# 关闭文件流
f.close()
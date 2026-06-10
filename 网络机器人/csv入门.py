# csv操作方式一
# 写
# with open("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,性别,年龄\n")
#     f.write("张润,女,20\n")
#     f.write("林忆宁,女,21\n")

# 读
with open("csv_data/01.csv","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 操作方式二
import csv
with open("csv_data/02.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","性别","年龄"])
    writer.writeheader() #写入表头
    writer.writerow({"姓名":"小王","性别":"男","年龄":"14"}) # 写入数据
    writer.writerow({"姓名":"小李","性别":"男","年龄":"14"})
    writer.writerow({"姓名":"小明","性别":"男","年龄":"14"})

# 读
with open("csv_data/02.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

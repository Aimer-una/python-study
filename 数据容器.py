# list_num = []
# for x in range(10):
#     num = int(input("请输入一个有效数字:"))
#     list_num.append(num)
# list_num.sort()
#
# print(list_num)
# print(list_num[0])
# print(list_num[len(list_num)-1])
#
# nums_sum = 0
# for s in list_num:
#     nums_sum += s
# print(nums_sum / len(list_num))

print("===================================================")
double_list = []
for x in range(1,21):
    double_list.append(x*x)
print(double_list)

num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
ans_list = []
for num in num_list:
    if num % 2 == 0:
        ans_list.append(num*num)
print(ans_list)

def triangle_area(low,high):
    """
    :param low: 底边
    :param high: 高
    :return: 面积
    """
    return low*high / 2

print(triangle_area(3,5))

def calculate_nums(content):
    """
    :param content: 用户传入的字符串
    :return: 字符串的元音字母的个数
    """
    ans = 0
    for c in content:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
           ans += 1
    return ans

print(calculate_nums(['a','b','c']))

def statistics_score(score_list):
    """
    统计学生分数列表
    :param score_list: 学生分数列表
    :return: 最高分，最低分，平均分
    """
    return max(score_list),min(score_list),sum(score_list)/len(score_list)
s_list = [99,56,33,41,67]
max_score,min_score,avg_score = statistics_score(s_list)
print("最高分:",max_score)
print("最低分:",min_score)
print("平均分:",avg_score)
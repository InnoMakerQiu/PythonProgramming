import time

# 给定 n 个正整数 a1,a2,…,an，你可以将它们任意排序。
# 现要将这 n 个数字连接成一排，即相邻数字首尾相接，组成一个数。
# 问，这个数最大可以是多少。
# 第一行输入一个正整数 n（1≤n≤20）。
# 第二行输入 n 个正整数 a1,a2,…,an（1≤a_i≤10^5）

from functools import cmp_to_key

from itertools import permutations

# 定义自定义比较函数
def compare(x, y):
    # 比较两个拼接结果
    if x + y > y + x:
        return -1  # x 应该排在 y 前面
    elif x + y < y + x:
        return 1  # y 应该排在 x 前面
    else:
        return 0  # x 和 y 相等

# 读取输入
n = int(input())
nums = input().split()
start_time = time.time()
# 对数字进行排序
nums_sorted = sorted(nums, key=cmp_to_key(compare))

# 将排序后的数字连接成结果
result = ''.join(nums_sorted)

# 打印结果
print(result)



end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

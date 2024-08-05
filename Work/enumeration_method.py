# 四平方和定理，又称为拉格朗日定理：
# 每个正整数都可以表示为至多 4 个正整数的平方和。
# 如果把 0 包括进去，就正好可以表示为 4 个数的平方和。
# 对于一个给定的正整数，可能存在多种平方和的表示法。
# 要求你对 4 个数排序：
# 0≤a≤b≤c≤d
# 并对所有的可能表示法按 a,b,c,d为联合主键升序排列，最后输出第一个表示法。
# 输入描述
# 程序输入为一个正整数 N(N<5×10^6)
# 输出描述
# 要求输出 4 个非负整数，按从小到大排序，中间用空格分开
# 题目来源四平方和：https://www.lanqiao.cn/courses/10606/learning/?id=566175&compatibility=false

import math

# # 枚举的范围为根号N/2<n<=根号N
# # 采用深度优先搜索的思想
# # 使用一个列表进行记录a,b,c,d的值，比如d=res_list[0]..a=res_list[3]
# # dfs函数中需要携带depth深度信息，res_num（for in range(depth): src_num-res_list[i])
# # 首先将x4的取值为
# res_lists = []
# my_list= [0,0,0,0]

# def dfs(depth,res_num):
#     if depth==3:
#         my_list[depth] = int(math.sqrt(res_num))
#         res_num = res_num - my_list[depth]**2
#         if res_num==0:
#             res_lists.append(list(reversed(my_list)))
#         return
#     max_range = int(math.sqrt(res_num))
#     min_range = int(math.sqrt(res_num/(4-depth)))
#     for i in range(max_range,min_range-1,-1):
#         # print(f"the depth : {depth}, the res_num : {res_num}")
#         # print(f"res_num: {res_num}, max_range: {max_range}, min_range: {min_range}, i: {i}")
#         my_list[depth] = i
#         num = res_num - i**2
#         dfs(depth+1,num)

# des_num = int(input())
# dfs(0,des_num)
# res_lists.sort()
# print(*res_lists[0], sep=' ')



import os
import sys
from math import sqrt
 
# print(sys.version)
# 下面是来源于https://lrl52.top/1146/python-lanqiaocup/
n = int(input())
l1 = int(sqrt(n))
for i in range(0, l1 + 1):
    l2 = int(sqrt(n - i * i))
    if l2 < i: break
    for j in range(i, l2 + 1):
        l3 = int(sqrt(n - i * i - j * j))
        if l3 < j: break
        for k in range(j, l3 + 1):
            t = int(sqrt(n - i * i - j * j - k * k))
            if t < k: break
            if i * i + j * j + k * k + t * t == n:
                print(i, j, k, t)
                sys.exit(0)

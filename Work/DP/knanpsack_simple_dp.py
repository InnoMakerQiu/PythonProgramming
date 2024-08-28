# 【题目描述】有一个箱子容量为V(正整数,0<V<20000),|同时有n个物品(0<n≤
# 30),每个物品有一个体积(正整数)。要求n个物品中,任取若干个装入箱内,使箱
# 子的剩余空间为最小。
# 【输入描述】输入第一行,一个整数,表示箱子容量。第二行,一个整数n,表示有n个
# 物品。接下来n行,分别表示这n个物品的各自体积。
# 【输出描述】输出一行,表示箱子剩余空间。
# 这道题可以通过动态规划（DP）来解决，其实质是一个“01背包问题”，目标是尽可能地填满箱子，从而使得箱子剩余空间最小。
# import os
# import sys

# def min_remaining_space(V, volumes):
#     if V <= 0:
#         return 0
#     dp = [0] * (V + 1)  # 初始化DP数组，容量为V

#     # 动态规划过程
#     for v in volumes:
#         if v > V:  # 如果物品体积超过箱子容量，跳过这个物品
#             continue
#         for j in range(V, v - 1, -1):  # 倒序遍历容量
#             dp[j] = max(dp[j], dp[j - v] + v)

#     # 输出箱子的最小剩余空间
#     return V - dp[V]

# # 示例输入
# V = int(input())  # 箱子容量
# n = int(input())  # 物品数量
# volumes = [int(input()) for _ in range(n)]  # 物品体积列表

# # 调用函数并打印结果
# print(min_remaining_space(V, volumes))

# 使用完全背包问题进行解决

# 状态定义，dp[i]代表，容量为i的背包，所拥有的最大价值
# 状态转移，dp[i] = max(dp[i],dp[i-ci]+wi)
# 初始状态为，dp[0]=0
# 计算顺序，整数i的范围为1-C

N,C = map(int,input().split())
c_list=[0]*N
w_list=[0]*N
for i in range(N):
    c_list[i],w_list[i] = map(int,input().split())

dp = [0]*(C+1)

for i in range(1,C+1):
    for j in range(N):
        if i >= c_list[j]:
            dp[i] = max(dp[i],dp[i-c_list[j]]+w_list[j])

print(dp[C])

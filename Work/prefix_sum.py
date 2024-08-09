# Prefix Sum
# 给定 n 个整数 a1,a2,⋅⋅⋅,an ，求它们两两相乘再相加的和。

# 这个问题可以表达为S_n=a_n*s_{n-1}+..a_{n-1}*s_{n-2}+...+a_2*s_1
# 求取前缀和


import time
from random import randint


total_num = int(input())
num_list = list(map(int,input().split()))
# total_num = 10
# num_list = []
# for i in range(total_num):
#     num_list.append(randint(1,1000))

# print(num_list)

start_time = time.time()

sum_list = []
sum =0
for i in range(total_num):
    sum+=num_list[i]
    sum_list.append(sum)
# print(sum_list)

sum=0
for i in range(total_num-1):
    sum += num_list[i+1]*sum_list[i]

print(sum)


end_time = time.time()
execution_time = end_time - start_time
print(execution_time)



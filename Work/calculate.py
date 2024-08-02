# 小蓝有一个整数 n。每分钟，小蓝的数都会发生变化，
# 变为上一分钟的数减去上一分钟的数的各个数位和。
# 例如，如果小蓝开始时的数为 23，则下一分钟变为 23−(2+3)=18，再下一分钟变为 18−(1+8)=9，
# 再下一分钟变为 9−9=0，共经过了 3 分钟变为 0。
# 给定一个正整数，请问这个数多少分钟后变为 0。

import os
import sys

def digit_sum(x):
    return sum(int(digit) for digit in str(x))

# # 采用暴力穷举的方法
def minutes_to_zero1(n):    
    minutes = 0
    while n > 0:
        n -= digit_sum(n)
        minutes += 1
    return minutes

# 发现规律，假设一个数可以拆分为m*10+n，那么每次相减过程为m*10-digit_sum(m)，这里我们关注m的变化即可
# 结果为m-(digit_sum(m)-1)//10-1，然后依次进行循环迭代直到m到0，然后step+1。
# 但是这种办法也行不通
def minutes_to_zero(n):
    step = 0
    n = n//10
    while n >0:
        n -= ((digit_sum(n)-1)//10+1)
        step+=1
    return step+1

n = int(input())
print(minutes_to_zero(n))

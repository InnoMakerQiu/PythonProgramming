# 这道题目要求我们判断每个输入的正整数 $$a_i$$ 是否可以表示为 
# $$x_1^{y_1} \times x_2^{y_2}$$ 的形式，
# 其中 $$x_1, x_2$$ 为正整数，$$y_1, y_2$$ 为大于等于2的正整数。


# 解决思路：
# 题目要求qi≥2,拆分:qi=k1y1+k2y2,k1,k2>0,y1,y2≥2。y2=2,y3=3可以保证所有qi>2均有非负整数解。
# 首先，我们先进行质因素分解，必须要满足的条件为每个质素对应的指数qi>=2。如果qi==1，那么不满足，输出no。
# 特殊情况处理，对于大于4000的质因数 p，其指数 q_i 只能是2、3或4。对于这些情况，只需判断a_i是否为某个数的平方或立方即可。

from math import *  # 导入数学模块，主要用于开方、幂操作等

N = 4000  # 定义4000以内的质数范围
prime = [0] * N  # 用于存储质数的数组
vis = [0] * N  # 标记数组，用于埃拉托斯特尼筛法
cnt = 0  # 质数计数器

#判断平方数
# 计算 x ** 0.5，得到的结果是浮点数，然后将其转换为整数类型 y。
# 由于浮点数表示的精度问题，y 可能比真实的整数平方根略小，所以增加判断条件，(y+1)**2==x。
def square_number(x):
    y = int(x ** 0.5)
    return y * y == x or (y + 1) * (y + 1) == x
#判断立方数
def cubic_number(x):
    y = int(x ** (1 / 3))
    return y ** 3 == x or (y + 1) ** 3 == x

# 首先使用埃拉托斯特尼筛法生成所有小于4000的质数，便于后续质因数分解
def E_sieve():
    global cnt
    for i in range(2, N):
        if not vis[i]:  # 如果i是质数
            cnt += 1
            prime[cnt] = i  # 记录质数
            for j in range(i * i, N, i):  # 标记i的所有倍数为非质数
                vis[j] = 1

def solve():
    a = int(input())  # 输入需要判断的整数a
    for i in range(1, cnt + 1):  # 遍历所有小于4000的质数
        c = 0
        while a % prime[i] == 0:  # 对a进行质因数分解
            a //= prime[i]
            c += 1
        if c == 1:  # 如果有质因数的指数为1，输出no
            print("no")
            return
    # 下面是进行快速指数检测
    if square_number(a):  # 如果a是平方数，输出yes
        print("yes")
        return
    if cubic_number(a):  # 如果a是立方数，输出yes
        print("yes")
        return
    print("no")  # 如果都不是，输出no

E_sieve()  # 执行埃拉托斯特尼筛法，生成质数表
T = int(input())  # 输入询问次数
for i in range(T):  # 处理每个询问
    solve()
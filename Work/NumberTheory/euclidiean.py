
def exgcd(a, b):
    if b == 0:
        return (1, 0)  # 如果 b 为 0，那么 gcd(a, b) = a，此时特解为 (1, 0)
    x, y = exgcd(b, a % b)  # 递归求解更小问题的特解
    print(x,y)
    return (y, x - (a // b) * y)  # 更新当前特解，返回 (y, x - (a // b) * y)


a, b = 6, 15
x, y = exgcd(a, b)  # 计算得到特解
print(x, y)  # 输出特解 x, y

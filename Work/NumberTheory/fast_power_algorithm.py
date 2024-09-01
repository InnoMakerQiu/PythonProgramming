# 给定b,p,k,求(b^p) mod k。其中2<b,p,k<10^18。
# 输入: 三个整数b,p,k。
# 输出: 输出(b^p) mod k。

def fastPow(a, n, mod):
    ans = 1
    while n:
        # 如果 n 的最低位是 1，则需要将当前的 a 乘到结果 ans 中
        if n & 1:
            ans = (ans * a) % mod
        # 当前幂次平方
        a = (a * a) % mod
        # 右移 n，处理下一个二进制位
        n >>= 1
    return ans

# 读取输入
b, p, k = map(int, input().split())
# 输出 (b^p) % k
print(fastPow(b, p, k))


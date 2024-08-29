# 统计区间 [1,b] 内每个数字（0到9）的出现次数，是一个典型的数位统计问题。
# 实现流程

def count_digits_up_to(x):
    """ Count the number of each digit in the range [1, x]. """
    
    # 预先计算 10 的各次方和数字出现次数的累加和
    ten = [1] * 15
    dp = [0] * 15
    cnt = [0] * 10
    
    # 计算 10 的幂和 dp 数组
    for i in range(1, 15):
        ten[i] = ten[i - 1] * 10
        dp[i] = dp[i - 1] * 10 + ten[i - 1]

    # 将 x 转换为字符串后反转以便从低位到高位处理
    n = list(map(int, str(x)))
    n.reverse()

    # 解决函数，用于计算各个数字的出现次数
    def solve():
        """ 主函数计算每个数字的个数。 """
        for i in range(len(n) - 1, -1, -1):
            # 计算当前数位的所有可能数字的贡献
            for j in range(10):
                cnt[j] += dp[i]*n[i]
            for j in range(n[i]):
                cnt[j] += ten[i]

            # 计算高位数字的贡献
            u = 0
            for j in range(i - 1, -1, -1):
                u = u * 10 + n[j]

            cnt[n[i]] += u + 1
            
            # 如果是最高位且为 0，修正前导 0 的贡献
            if i == 0:
                cnt[0] -= ten[i]

    solve()
    return cnt

# 输入和输出处理
b = int(input())
result = count_digits_up_to(b)
print(' '.join(map(str, result)))







#   用于计算矩阵 A 和矩阵 B 的乘积。
#   查两个矩阵的尺寸是否匹配（矩阵 A 的列数是否等于矩阵 B 的行数）。
#   使用三重循环计算矩阵乘法的每个元素。
def multi(A, B):
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    if n1 != m2: return None  # 检查矩阵A的列数是否等于矩阵B的行数
    C = [[0] * n2 for i in range(m1)]  # 初始化结果矩阵C
    for i in range(m1):
        for k in range(n1):
            for j in range(n2):
                C[i][j] += A[i][k] * B[k][j]  # 计算矩阵乘法
    return C

# 用于计算矩阵 A 的 n 次幂。
# 初始化结果矩阵 res 为单位矩阵（对角线上的元素为1，其余元素为0）。
# 使用 while 循环处理每一位的幂次：
# 如果当前位是 1，则将当前的矩阵 A 乘到结果 res 中。
# 将矩阵 A 自乘一次以计算更高的幂次。
# 右移 n，处理下一个二进制位。
def power(A, n):
    N = len(A)  # 矩阵的大小
    res = [[0] * N for i in range(N)]  # 初始化结果矩阵为单位矩阵
    for i in range(N):
        res[i][i] = 1
    while n:
        if n % 2: res = multi(res, A)  # 如果当前位是1，则乘上当前的矩阵A
        A = multi(A, A)  # 将矩阵A自乘一次，得到更高次幂的矩阵
        n //= 2  # 右移一位，处理下一个二进制位
    return res

N,M = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
res = power(A,M)
for i in range(N):
    print(" ".join(str(item) for item in res[i]))



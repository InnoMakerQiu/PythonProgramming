import os,sys

n, m, k = map(int, input().split())
tot = (1<<m) -1
# tot:二进制是m个1,表示所有m种口味
dp = [-1 for _ in range(1 << 20)]
dp[0] = 0
kw = []
for _ in range(n):
    kw.append([int(i) for i in input().split()])
for c in kw:    # 选用c遍历每包糖果
    #用c遍历每包糖果
    tmp = 0
    for x in c: tmp |= (1<<(x-1))
        # 用x遍历这包糖果的口味
    for i in range(tot+1):
        if(dp[i]==-1): continue #已存在得到口味i的最少糖果包数量
        newcase = i | tmp
        if (dp[newcase]==-1) or (dp[newcase] > dp[i] + 1):
           dp[newcase] = dp[i] + 1
print(dp[tot])
#得到所有口味tot的最少糖果包数


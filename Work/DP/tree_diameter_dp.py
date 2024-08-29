# 在树形结构中，树的直径定义为树中任意两节点之间最长的路径长度。
# 求解树的直径问题可以使用动态规划 (DP) 的方法，通过深度优先搜索 (DFS) 进行递归计算。

def dfs(u):
    global ans
    vis[u] = 1  # 标记节点 u 已访问
    for v, c in tree[u]:  # 遍历节点 u 的邻居 v 以及边权 c
        if vis[v] == 1:  # 如果 v 已访问过，跳过
            continue
        dfs(v)  # 递归计算子节点 v 的 dp 值
        ans = max(ans, dp[u] + dp[v] + c)  # 更新全局最大值 ans，可能为两子树路径的和
        dp[u] = max(dp[u], dp[v] + c)  # 更新当前节点 u 的 dp 值

n = int(input())

# 树的构建过程
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    v1,v2,edge = map(int,input().split())
    tree[v1].append((v2,edge))
    tree[v2].append((v1,edge))

# 计算树的直径
ans = 0  # 初始化答案为0，代表目前的最大路径长度（树的直径）

# vis数组用于标记节点是否被访问过，初始化为0，长度为n+1（假设节点编号从1到n）
vis = [0 for i in range(n+1)]

# dp数组用于存储以每个节点为根的子树中，从该节点出发到达的最远路径长度
dp = [0 for i in range(n+1)]

# 从节点1开始进行深度优先搜索，计算树的直径
dfs(1)

# 打印最终的答案
print(ans * 10 + ans * (ans + 1) // 2)

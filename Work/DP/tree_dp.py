# 作在树上寻找一个最大权值子树的问题
import sys

# 在算法执行过程中，记得需要设置递归深度
sys.setrecursionlimit(50020)


def calculate_tree_score(n, values, edges):
    from collections import defaultdict

    # 构造树
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # 初始化 DP 数组
    dp = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        dp[u] = values[u - 1]  # 注意，这里values是0-indexed，而节点编号是1-indexed
        for v in tree[u]:
            if not visited[v]:
                dfs(v)
                dp[u] += max(dp[v], 0)  # 如果dp[v]是正数，我们才加上
        
    # 从任意一个节点开始DFS
    dfs(1)
    
    # 求所有dp中的最大值
    max_score = max(dp)
    return max_score

# 输入处理
n = int(input())
values = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# 计算树的最大评分
print(calculate_tree_score(n, values, edges))
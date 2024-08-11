import sys

class UnionFindWithPathCompression:
    def __init__(self, n):
        # 注意需要正确进行初始化操作
        self.parent = list(range(n+1))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY


N,M = map(int,input().split())
union_list = []

for i in range(M):
    union_list.append(list(map(int,input().split())))

# print(union_list)

union_find_set = UnionFindWithPathCompression(N)
# print_str = ""
for i in range(M):
    op = union_list[i][0]
    x = union_list[i][1]
    y = union_list[i][2]
    if op == 1:
        union_find_set.union(x,y)
    if op == 2:
        root_x = union_find_set.find(x)
        root_y = union_find_set.find(y)
        if root_x == root_y:
            print("YES")
        else:
            print("NO")

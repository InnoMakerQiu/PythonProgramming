import sys
sys.setrecursionlimit(60000) # 设置递归深度

# 对所有网格进行遍历
# 如果该网格中有#，那么进行深度优先搜索操作，对该联通块进行完整遍历
# 同时进行访问记录，访问的元素会被置为1
# 如果某个联通块中的一个元素的上下左右都出现了#
# 那么表明该岛屿不会被淹没

N = int(input())
grid = []
for i in range(N):
    str_list = list(input())
    grid.append(str_list)

# 用来记录是否被访问过，其中置为1代表被访问过
visited_grid = [[0]*N for _ in range(N)]


def dfs(x,y):
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    global is_island
    # 首先进行越界检查
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    # 判断是否为岛屿
    if grid[x][y] == '.':
        return
    # 判断是否已经访问过
    if visited_grid[x][y] == 1:
        return
    visited_grid[x][y]=1
    # 判断是否存在不会被淹没的岛屿
    if grid[x+1][y]=='#' and grid[x-1][y]=='#' and grid[x][y+1]=='#' \
        and grid[x][y-1]=="#":
        is_island = 1
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        dfs(nx,ny)        
    
    

count=0
island_count = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == '#' and visited_grid[i][j]==0:
            # print(i,j)
            # 用来记录不会被淹没的岛屿
            is_island =0
            dfs(i,j)
            # print(is_island)
            count+=1
            island_count+= is_island

print(count - island_count)





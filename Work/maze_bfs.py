# 下图给出了一个迷宫的平面图，其中标记为 1 的为障碍，标记为 0 的为可以通行的地方。
# 010000
# 000100
# 001001
# 110000
# 迷宫的入口为左上角，出口为右下角，在迷宫中，
# 只能从一个位置走到这 个它的上、下、左、右四个方向之一。
# 对于上面的迷宫，从入口开始，可以按 DRRURRDDDR 的顺序通过迷宫，
#  一共 10 步。其中 D、U、L、R分别表示向下、向上、向左、向右走。 
# 对于下面这个更复杂的迷宫（3030 行 5050 列），请找出一种通过迷宫的方式，
# 其使用的步数最少，在步数最少的前提下，请找出字典序最小的一个作为答案。
# 请注意在字典序中 D<L<R<U。

# 解题思路，通过bfs算法进行最短路径求解
# 每个点都记录其的前驱节点的信息
# 找到终点后，然后再进行回溯操作，得到完整的路径

from collections import deque
import sys
# 定义四个方向以及对应的移动
DIRECTIONS = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

maze = []
for i in range(0, 30):
    maze.append(list(input()))


rows, cols = len(maze),len(maze[0])
queue = deque([(0,0)])
visited = [[0] * cols for _ in range(rows)]
visited[0][0]= 1

# 前驱节点的信息图
pre_info_map = [[' ']*cols for _ in range(rows)]

def find_path():
    path = deque()
    x,y = rows-1,cols-1
    while x != 0 or y!=0:
        for direction,dx,dy in DIRECTIONS:
            if pre_info_map[x][y] == direction:
                path.appendleft(direction)
                x = x - dx
                y = y - dy
    # 进行path打印
    path_str = ''
    for dir in path:
        path_str += str(dir)
    print(path_str)


while queue:
    x,y = queue.popleft()
    # 如果到达出口，则返回路径
    if (x,y) == (rows-1,cols-1):
        find_path()
        sys.exit(0)
    # 按照指定顺序进行节点扩展
    for direction,dx,dy in DIRECTIONS:
        nx,ny = x+dx,y+dy

        if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] == '0':
            visited[nx][ny] = 1  # 标记新节点已访问
            pre_info_map[nx][ny] = direction
            queue.append((nx, ny))
        




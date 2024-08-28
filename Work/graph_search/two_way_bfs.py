# "012345678" -> "087654321"，其中只有0可以和其他元素替换，
# 可以向左或者向右的一到两个偏移量进行替换，步数要求为最少
# 可以使用双向广播的算法对步数进行计算

from collections import deque

def get_neighbors(state):
    """返回所有合法的移动"""
    neighbors = []
    cur_index = state.index('0')# 当前0的位置
    moves = [ -1, -2, 1, 2]  # 左右移动偏移量

    for dindex in moves:
        new_index = (cur_index+dindex)%9
        # 生成新状态
        new_state = list(state)
        new_state[cur_index], new_state[new_index] = new_state[new_index], new_state[cur_index]
        neighbors.append(''.join(new_state))
    
    return neighbors

def bidirectional_bfs(start, target):
    if start == target:
        return 0
    
    # 双向搜索的队列和访问集合
    forward_queue = deque([start])
    backward_queue = deque([target])
    
    forward_visited = {start: 0}
    backward_visited = {target: 0}
    
    # 双向 BFS
    while forward_queue and backward_queue:
        # 从起点扩展
        result = bfs_step(forward_queue, forward_visited, backward_visited)
        if result != -1:
            return result
        
        # 从终点扩展
        result = bfs_step(backward_queue, backward_visited, forward_visited)
        if result != -1:
            return result
    
    return -1  # 如果没有找到解

def bfs_step(queue, visited, other_visited):
    """扩展一层"""
    state = queue.popleft()
    step = visited[state]
    
    for neighbor in get_neighbors(state):
        if neighbor in visited:
            continue
        if neighbor in other_visited:
            return step + 1 + other_visited[neighbor]  # 相遇，返回步数
        queue.append(neighbor)
        visited[neighbor] = step + 1
    
    return -1

# 初始状态和目标状态
start = "012345678"
target = "087654321"

# 调用双向BFS
result = bidirectional_bfs(start, target)
print(result)
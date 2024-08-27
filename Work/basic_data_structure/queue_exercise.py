from collections import deque
import sys

# 输入描述
# 第一行一个数字N。 接下来N 行，每行第一个数字为操作命令：1. 入队、2. 出队并输出、
# 3. 计算队中元素个数并输出。
# 输出描述
# 若干行每行显示一个 2 或 3 命令的输出结果。
# 注意：2. 出队命令可能会出现空队出队（下溢），请输出“no”，并退出。

N = int(input())
queue = deque()
for i in range(N):
    opt_list = list(map(int,input().split()))
    if opt_list[0] == 1:
        queue.append(opt_list[1])
    elif opt_list[0] == 2:
        if queue:
            print(queue.popleft())
        else:
            print("no")
            sys.exit(0)
    elif opt_list[0] == 3:
        print(len(queue))


from math import inf
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Since the problem is equilavent to the single source shortest problem 
        # and has nonnegative weights on all edges,
        # dijkstra is applicable.

        # initialize the single-source graph(G,s)
        # The adjacent list is more convenient to use, so it is chosen.
        g_table = [[] for _ in range(n)]
        for x,y,time in times:
            g_table[x-1].append((y-1,time))
        # print(g_table)

        # q_heapq contains the vertices which belongs to set(g_matrix.v-s_list)
        # use priority queue to extract minimum value from q_heapq quickly
        q_heapq = [(0,k-1)]

        # record the shortest distance from k
        dis_list = [inf]*n
        dis_list[k-1] = 0

        # extract min vertex u from q_heapq, then add u into s_list and relax the edge leaving u
        # then update the relaxed edge in q_heapq until it's empty.
        while q_heapq:
            # print("q_heapq")
            # print(q_heapq)
            w1,u = heapq.heappop(q_heapq)
            # If w1 > result_list[u-1], it indicates w1 is outdated. Skip it.
            if w1 > dis_list[u]:
                continue
            dis_list[u]=w1
            # relax the edge leaving u
            for v,w2 in g_table[u]:
                new_dis = w1+w2
                if new_dis < dis_list[v]:
                    heapq.heappush(q_heapq,(new_dis,v))
        mx =  max(dis_list)
        return mx if mx < inf else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
solution = Solution()
result = solution.networkDelayTime(times,4,2)
print(result)

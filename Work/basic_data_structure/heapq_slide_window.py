import heapq
from typing import List

class Solution:
    # This function finds the maximum element in each sliding window of size k.
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # The algorithm uses a priority heap to maintain the index of the potential max_num
        window_heap = []
        n = len(nums)
        for i in range(k):
            heapq.heappush(window_heap,(-nums[i],i))
        
        record_list=[]
        record_list.append(-window_heap[0][0])

        # slide the window
        for i in range(k,n):
            heapq.heappush(window_heap,(-nums[i],i))
            # remove element not within the sliding window 
            while window_list[0][1] < i-k+1:
                heapq.heappop(window_heap)
            # print("window heap")
            # print(window_heap)
            record_list.append(-window_heap[0][0])
        return record_list

nums = [1,-1]
solution  = Solution()
print(solution.maxSlidingWindow(nums,1))



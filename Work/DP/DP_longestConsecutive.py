from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) DP to track the consecutive segment length

        # Define the status - hash_dict stores segment lengths
        # hash_dict(right)=hash_dict(left)=right-left+1 (length).
         
        # Transition. Update the segment length if nums[i] is not part of any segment. 

        # Initialization. hash_dict={}.

        hash_dict={}
        res = 0
        for num in nums:
            if hash_dict.get(num,0):
                continue
            left_len = hash_dict.get(num-1,0)
            right_len = hash_dict.get(num+1,0)
            len = left_len+right_len+1
            # update the continuous segment
            hash_dict[num]=1
            hash_dict[num-left_len] = len
            hash_dict[num+right_len] = len
            res = max(len,res)
            # print(num,hash_dict,res)
        return res

sol = Solution()
count = sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(count)

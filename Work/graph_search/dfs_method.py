# https://leetcode.cn/problems/subsets/description/
# 采用回溯算法进行求解

nums = [1,2,3]

# def dfs(depth:int,max_depth:int,path:list,path_list:list):
#     if depth == max_depth:
#         path_list.append(path.copy())
#         return
    
#     dfs(depth+1,max_depth,path,path_list)
#     path.append(nums[depth])
#     dfs(depth+1,max_depth,path,path_list)
#     path.pop() # 进行操作撤销
    
    
# max_depth = len(nums)
# path_list = []
# dfs(0,max_depth,[],path_list)
# print(path_list)


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth:int,max_depth:int,path:list,path_list:list):
            if depth == max_depth:
                path_list.append(path.copy())
                return
            
            dfs(depth+1,max_depth,path,path_list)
            path.append(nums[depth])
            dfs(depth+1,max_depth,path,path_list)
            path.pop() # 进行操作撤销
            
            
        max_depth = len(nums)
        path_list = []
        dfs(0,max_depth,[],path_list)
        return path_list

s = Solution()
print(s.subsets(nums))



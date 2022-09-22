class Solution:
    def subsetsWithDup(self, nums):
        res=[]
        nums.sort()
        
        def dfs(index=0, subset=[]):
            if index >= len(nums):
                res.append(subset[::])
                return
            
            # all subsets containing nums[index]
            subset.append(nums[index])
            dfs(index+1, subset)
            subset.pop()
            
            # all subsets not containing nums[index]
            while index+1 < len(nums) and nums[index+1] == nums[index]:
                index += 1
            dfs(index+1, subset)
        dfs()
        return res
                
            
        
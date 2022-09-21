class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(length, cur_index, cur_array):
            if  cur_index >= length:
                res.append(cur_array.copy())
                return
            cur_array.append(nums[cur_index])
            backtrack(length, cur_index+1, cur_array)
            cur_array.pop()
            backtrack(length, cur_index+1, cur_array)
        
        backtrack(len(nums), 0, [])
        return res
        
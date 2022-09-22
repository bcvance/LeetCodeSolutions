class Solution1:
    def permute(self, nums):
        res = []
        
        def backtrack(index=0, used=set(), permutation=[]):
            for num in nums:
                if index >= len(nums):
                    res.append(permutation.copy())
                    return
                if num not in used:
                    used.add(num)
                    permutation.append(num)
                    backtrack(index+1, used, permutation)
                    used.remove(num)
                    permutation.pop()
        backtrack()
        return res




class Solution2:
    def permute(self, nums):
        result = []

        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        return result

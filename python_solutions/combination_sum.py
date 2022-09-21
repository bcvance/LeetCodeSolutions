class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i=0, total=0, combination=[]):
            if i >= len(candidates) or total > target:
                return
            elif total == target:
                res.append(combination.copy())
                return
            for index in range(i, len(candidates)):
                combination.append(candidates[index])
                dfs(index, total+candidates[index], combination)
                combination.pop()
        dfs()
        return res
            
        
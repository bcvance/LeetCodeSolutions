class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        res = []
        
        def dfs(i=0, total=0, combination=[]):
            if total == target:
                res.append(combination[::])
                return
            if i >= len(candidates) or total > target:
                return
            combination.append(candidates[i])
            dfs(i+1, total+candidates[i], combination)
            combination.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, total, combination)
        dfs()
        return res
class Solution:
    def letterCombinations(self, digits: str):
        key_map = {
            2: 'abc', 
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
            }
        if digits == "":
            return []
        res = []
        combo = []

        def backtrack(index=0):
            if index >= len(digits):
                res.append("".join(combo[::]))
                return
            for letter in key_map[int(digits[index])]:
                combo.append(letter)
                backtrack(index+1)
                combo.pop()
        backtrack()
        return res

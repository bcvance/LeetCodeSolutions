class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        res_len = 0

        # odd length 
        for i in range(len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res_len = r-l+1
                    res = s[l:r+1]

                l -= 1
                r +=1
        # even length
        for i in range(len(s)):
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res_len = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res
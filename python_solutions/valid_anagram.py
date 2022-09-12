class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_dict = {}
        t_letter_dict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_letter_dict[s[i]] = 1 + s_letter_dict.get(s[i], 0)
            t_letter_dict[t[i]] = 1 + t_letter_dict.get(t[i], 0)
        for key in s_letter_dict:
            if s_letter_dict[key] != t_letter_dict.get(key, 0):
                return False
        return True
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):                
        counts_dict = defaultdict(list)

        for index, word in enumerate(strs):
            counts = [0 for i in range(26)]
            for letter in word:
                counts[ord(letter)-ord('a')] += 1
            counts_dict[tuple(counts)].append(strs[index])
        return counts_dict.values()
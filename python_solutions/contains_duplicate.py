class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict[num] = 1
        return False
class Solution:
    def twoSum(self, nums, target: int):
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in nums_dict and nums_dict[looking_for] != i:
                return [i, nums_dict[looking_for]]
        
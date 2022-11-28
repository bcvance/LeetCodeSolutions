class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0
        if len(nums) == 1:
            return nums[0]

        for n in nums[:len(nums)-1]:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        max1 = rob2

        rob1, rob2 = 0, 0
        for n in nums[1:]:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        max2 = rob2

        return max(max1, max2)
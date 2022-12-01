class Solution:
    def maxProduct(self, nums) -> int:
        max_product = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            temp = cur_max
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(n * temp, n * cur_min, n)
            max_product = max(max_product, cur_max)

        return max_product
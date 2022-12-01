class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2:
            return False

        sums = set()
        sums.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            tmp = sums.copy()
            for sum1 in tmp:
                sums.add(sum1 + nums[i])
                if target in sums:
                    return True
        return False
            
class Solution:
    def productExceptSelf(self, nums):
        output = ["" for i in range(len(nums))]
        product = 1
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= product
            product *= nums[i]
        return output

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
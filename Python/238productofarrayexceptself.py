# How it works:
# create an array with the same length as nums 
# initialize left_product as 1 so it can be multiplied
# for each number in the length of nums, multiply
# left_product times nums 1 less than the current index
# multiply left_product times output with the same index
# then do the same for the right, except right_product is multiplied
# by index 1 more than current index
#then return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            output[i] *= left_product
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            output[i] *= right_product
        return output

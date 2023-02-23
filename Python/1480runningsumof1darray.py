# How it works:
# create array of size nums
# initialize sum and ptr at 0
# while the pointer is still in the range of nums,
# add the number of the pointer's position to sum
# add to output of the pointer's position the sum
# add 1 to the pointer
# repeat until ptr catches up with nums
# return output

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)
        sum = 0
        ptr = 0
        while ptr < len(nums):
            sum += nums[ptr]
            output[ptr] = sum
            ptr += 1
        return output
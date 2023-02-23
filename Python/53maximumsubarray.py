# How it works:
# the maximum is initiated as the first element and the current sum
# is initiated as 0
# for each number in the list, add it to the sum
# if the sum is less than 0, set it to 0
# check if the max subarray is larger than the current sum
# if it is, keep it the same, otherwise replace it
# keep going til all of the numbers are iterated through



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
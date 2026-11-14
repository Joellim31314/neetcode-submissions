class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runTotal=0
        bestTotal=nums[0]
        l=0
        r=0

        while r<len(nums):
            runTotal += nums[r]
            if runTotal<0:
                l = r+1
            if runTotal>bestTotal:
                bestTotal = runTotal
            r+=1
            if l == r:
                runTotal=0
        return bestTotal



class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = nums[0]
        
        while l<=r:
            #start by check whether crrrent window is fully sorted if it is than compare ans to left most num and return the smallest 
            if nums[l]< nums[r]:
                ans = min(ans,nums[l])
                return ans
            mid = (l+r)//2
            ans = min(ans,nums[mid])#this is a defencsive mechanism because it always throw away mid in both branches so if mid just so happen to be the smallest num than it will skip it by accident
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return ans
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        RES = [1]*n
        PREF =[1]*n
        SUFF =[1]*n
        for i in range(1,n):
            PREF[i] =  PREF[i-1] * nums[i-1]
        for i in range (n-2,-1,-1):
            SUFF[i] = SUFF[i+1] * nums[i+1]
        for i in range (n):
            RES[i] = PREF[i] * SUFF[i]
        return RES



            
        
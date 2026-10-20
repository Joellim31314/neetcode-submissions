class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] >= nums[r]:
                l = m+1
            else:
                r = m
        s = l
        l = 0
        r = len(nums)-1
        print(s)
        if target >= nums[s] and target <= nums[r]:
            l = s
        else:
            r = s - 1 
        print(l)
        print(r)
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
        
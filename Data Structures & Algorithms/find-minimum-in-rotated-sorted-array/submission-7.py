class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
# u could only solve this by comparing mid num to right and not the other way around because think of it like its nunmber moving in anti clock wise which mean they are always moving right in a cycle 
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[l]
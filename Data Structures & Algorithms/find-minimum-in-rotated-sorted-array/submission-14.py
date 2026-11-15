class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
# u could only solve this by comparing mid to right and not the other way around because think of it like its number moving in clock wise which mean they are always moving right in a cycle 
# if we were to compare mid to l than we wont be able to differiate between [3, 4, 5, 1, 2] and [1, 2, 3, 4, 5]
# because if mid>r that tells you the smallest num is between mid and r
#else mid<r meaning between mid to r is sorted 
#again num is moving anti clockwise so r should never skip a num as the next number might be lowest which is why r = mid
#but left can jump a number if mid>r than current mid cant be the answer since theres definitely a smaller answer 
#but opposite would always work 
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[l]
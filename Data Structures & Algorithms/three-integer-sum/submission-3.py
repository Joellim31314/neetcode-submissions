class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output= []
        print(nums)
        for i in range(len(nums)):
            
            if i > 0 and nums[i]==nums[i-1]:
                continue 
            second = i + 1
            third = len(nums)-1
            while second < third:
                if nums[i] + nums[second] + nums[third] > 0:
                    third -=1
                elif nums[i] + nums[second] + nums[third] < 0:
                    second+=1
                else:
                    output.append([nums[i],nums[second],nums[third]])
                    second+=1
                    third-=1
                    while nums[second] == nums[second -1] and second < third:
                        second+=1
                    while nums[third] == nums[third + 1] and second < third:
                        third-=1
        return output
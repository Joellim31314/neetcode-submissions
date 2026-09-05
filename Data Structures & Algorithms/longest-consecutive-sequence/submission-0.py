class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) in uniqueNums:
                continue
            else:
                temp=1
                while (i+1) in uniqueNums:
                    temp+=1
                    i+=1
                if temp>longest:
                    longest = temp
        return longest




        
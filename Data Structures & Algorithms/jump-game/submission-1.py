class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest=0
        for i,v in enumerate(nums):
            if i<=furthest:
                if (i+v)>furthest:
                    furthest = i+v
            else:
                return False
            if furthest == len(nums)-1:
                return True
        return True


                                                 
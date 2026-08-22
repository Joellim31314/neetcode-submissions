class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashsets = set()
        for i in nums:
            if i in hashsets:
                return True
            hashsets.add(i)
        return False
                

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        ans = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1

            if (r-l+1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l],0)-1
                l+=1
            if (r-l+1)>ans:
                ans = r-l+1
        return ans
            



        
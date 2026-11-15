class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charNum = {}
        ans = 0
        for r,v in enumerate(s):
            charNum[v] = charNum.get(v,0)+1
            if max(charNum.values()) + k < r-l+1:
                charNum[s[l]]-=1
                l+=1
            if r-l+1>ans:
                ans = r-l+1
        return ans
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0 
        l = 0
        r = len(heights) - 1
        while l != r:
            vol = max(vol,(min(heights[l],heights[r])*(abs(l-r))))
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return vol
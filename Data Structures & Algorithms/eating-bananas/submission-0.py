class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end = max(piles)
        start = 1
        ans = 1
        while start <= end:
            mid = (end + start)//2
            eatTime = 0
            for i in piles:
                eatTime= eatTime + (-(-i//mid))
            if eatTime > h:
                start = mid + 1
            else:
                end = mid - 1
                ans = mid
        return ans 


#k is number of banana eat per hour
#if k>piles[i][j] it will still be one pile in an hour so you can jump to eat another pile even if you have extra time
#find the edge of k where you wont be able to finish all piles within h hours 
#1 to highest value of banana in a pile
# since we can utilise the logic that max speed needed will always be number of piles so we get a range that we can test from therefore binary search from these list of speed

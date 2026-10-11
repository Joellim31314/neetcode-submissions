class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1)-1
        s1Char = {}
        s2Char = {}
        for i in range(len(s1)):
            s1Char[s1[i]] = s1Char.get(s1[i],0) + 1
        for i in range(r+1):
            s2Char[s2[i]] = s2Char.get(s2[i],0) + 1
        while r < len(s2):
            if s1Char ==s2Char:
                return True
            if r == len(s2)-1:
                return False

            s2Char[s2[l]] -= 1
            if s2Char[s2[l]] == 0:
                del s2Char[s2[l]]
            l+=1
            r+=1
            s2Char[s2[r]] = s2Char.get(s2[r],0)+1


            

         
        
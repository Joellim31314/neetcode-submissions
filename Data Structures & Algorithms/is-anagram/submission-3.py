class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        mapS, mapT = {},{}
        for i in s:
            mapS[i] = mapS.get(i,0)+1
        for j in t:
            mapT[j] = mapT.get(j,0)+1
        return mapS == mapT


        
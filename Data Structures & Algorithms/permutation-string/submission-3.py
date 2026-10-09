class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        temp = {}
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i],0)+1
        for r in range(len(s2)):
            temp = count.copy()  
            while  r <len(s2) and s2[r] in temp and temp[s2[r]] > 0 :
                temp[s2[r]]-=1
                r+=1 
            if max(temp.values()) == 0:
                return True
        return False
            





#l and r keep moving until it start matching than only r move

            
        
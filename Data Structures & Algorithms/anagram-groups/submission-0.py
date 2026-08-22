class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        position = {}

        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord("a")] += 1
            if tuple(count) in position:
                position[tuple(count)].append(i)
            else:
                position[tuple(count)] = [i]
        outcome = []
        for i in position:
            outcome.append(position[i])
        return outcome 





                
        
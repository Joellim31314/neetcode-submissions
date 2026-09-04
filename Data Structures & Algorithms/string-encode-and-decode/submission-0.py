class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for i in strs:
            ans.append(str(len(i)))
            ans.append("#")
            ans.append(i)
        result = "".join(ans)
        return result




    def decode(self, s: str) -> List[str]:
        output = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            output.append(s[i:j])
            i = j
        return output
            
            
            


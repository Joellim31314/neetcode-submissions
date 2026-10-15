class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combined = list(zip(position,speed))
        combined.sort()
# enumerate return index position + value of that index so if you want to access current value and nested value than just remove enumerate
        for p,s in combined:  
            while stack and (target-p)/s >= stack[-1]:
                stack.pop()
            stack.append((target-p)/s)


        return len(stack) 
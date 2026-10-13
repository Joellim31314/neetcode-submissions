class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validMatch = {")" : "(" , "]" : "[" , "}" : "{"}
        for i in s:
            if i in validMatch:
                if len(stack) == 0:
                    return False
                if validMatch[i] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
#
#if stack is empty by end of it than return true else false
        
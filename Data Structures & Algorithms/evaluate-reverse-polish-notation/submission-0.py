class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i,v in enumerate(tokens):
            if v == "+":
                a,b = stack.pop(),stack.pop()
                stack.append(b+a)
            elif v == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif v == "*":
                a,b = stack.pop(),stack.pop()
                stack.append(b*a)
            elif v == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(v))
        return stack[0]
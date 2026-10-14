class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures) # 0 is a good default as everything thats not answer at end of loop is automatically 0
        stack = []
        for i,t in enumerate(temperatures):
            while stack and temperatures[i]>stack[-1][0]:
                temp,index = stack.pop()
                output[index] = i - index

            stack.append([t,i])
        return output



        
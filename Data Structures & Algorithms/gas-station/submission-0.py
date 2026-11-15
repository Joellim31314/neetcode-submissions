class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        position = 0
        if sum(gas)< sum(cost):
            return -1
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank<0:
                tank = 0
                position = i+1
        return position

                

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            residue = (-heapq.heappop(stones))-(-heapq.heappop(stones))
            if residue == 0:
                continue
            else:
                heapq.heappush(stones,-residue)
        print(stones)
        if len(stones)>0:
            return -stones[0]
        else:
            return 0



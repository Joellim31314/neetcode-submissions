class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i in points:
            x,y = i
            d=((x-0)**2+(y-0)**2)**0.5
            heapq.heappush(dis,(d,[x,y]))
        res = []
        for y in range(k):
            distance,coor = heapq.heappop(dis)
            res.append(coor)
        return res
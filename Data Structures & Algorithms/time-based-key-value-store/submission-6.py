class TimeMap:

    def __init__(self):
        self.storeV = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storeV:
            self.storeV[key] = []
        self.storeV[key].append([timestamp,value])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storeV or timestamp < self.storeV[key][0][0]:
            return ""
        l = 0
        r = len(self.storeV[key])-1

        while l <= r:
            mid = (r + l)//2
            if timestamp>self.storeV[key][mid][0]:
                l = mid+1
            elif timestamp == self.storeV[key][mid][0]:
                return self.storeV[key][mid][1]
            else:
                r = mid-1
        return self.storeV[key][r][1]
        

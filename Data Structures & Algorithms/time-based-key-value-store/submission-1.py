class TimeMap:
    # { key1 : [(t1, value), (t2, value)], ... }
    def __init__(self):
        self.time_map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        vals = self.time_map[key]
        l = 0
        r = len(vals)-1
        result = ""
        while l <= r:
            m = (l+r)//2
            if timestamp >= vals[m][0]:
                l = m + 1
                result = vals[m][1]
            else:
                r = m - 1
        return result



        

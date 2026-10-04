class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap.get(key)
        if not arr:
            return ""
        l = 0
        r = len(arr) -1 
        closest = -1
        while(l<=r):
            m = int((l+r)//2)
            if (arr[m][1] > timestamp):
                r = m-1
            elif (arr[m][1] < timestamp):
                closest = m
                l = m+1
            elif (arr[m][1] == timestamp):
                return arr[m][0]
        if closest != -1:
            return arr[closest][0]
        return ""    


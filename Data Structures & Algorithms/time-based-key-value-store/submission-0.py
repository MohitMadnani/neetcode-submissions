class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []

        self.timeMap[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        arr = self.timeMap[key]
        L = 0
        R = len(arr) - 1
        res = ""

        while L <= R:

            mid = (L+R) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]

            elif arr[mid][0] < timestamp:
                res = arr[mid][1]
                L = mid + 1
            else:
                R = mid - 1

        return res        

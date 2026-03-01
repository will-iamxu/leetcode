class MedianFinder:

    def __init__(self):
        self.s = []
        self.l = []

    def addNum(self, num: int) -> None:
        if self.l and num > self.l[0]:
            heapq.heappush(self.l, num)
        else:
            heapq.heappush(self.s, num * -1)
        
        if len(self.s) > len(self.l) + 1:
            val = heapq.heappop(self.s)
            heapq.heappush(self.l, -1 * val)
        if len(self.l) > len(self.s) + 1:
            val = heapq.heappop(self.l)
            heapq.heappush(self.s, -1 * val)

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -1 * self.s[0]
        if len(self.l) > len(self.s):
            return self.l[0]
        return (-1 * self.s[0] + self.l[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
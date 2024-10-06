# https://leetcode.com/problems/find-median-from-data-stream/description/
class MedianFinder:
    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.stream, num)

    def findMedian(self) -> float:
        length = len(self.stream)
        if length % 2 == 0:
            return (self.stream[length // 2 - 1] + self.stream[length // 2]) / 2
        else:
            return self.stream[length // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

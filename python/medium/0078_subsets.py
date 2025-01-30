# https://clemson.zoom.us/my/bartk
class Solution:
    def addNum(self, num):
        temp = copy.deepcopy(self.res)
        length = len(self.res)

        for i in range(length):
            self.res[i].append(num)

        self.res = temp + self.res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        for num in nums:
            self.addNum(num)
        return self.res

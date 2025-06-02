# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        for i in range(len(grid)):
            rowMax.append(max(grid[i]))
        
        colMax = []
        for i in range(len(grid)):
            maxVal = 0
            for j in range(len(grid[i])):
                maxVal = max(maxVal, grid[j][i])
            colMax.append(maxVal)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rowMax[i], colMax[j]) - grid[i][j]
        return res

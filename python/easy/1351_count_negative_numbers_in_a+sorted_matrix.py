# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                count += len(grid[i])
            else:
                if grid[i][-1] < 0:
                    l = 0
                    r = len(grid[i]) - 1
                    while l <= r:
                        mid = l + (r - l) // 2
                        if grid[i][mid] >= 0:
                            l = mid + 1
                        else:
                            r = mid - 1
                    count += len(grid[i]) - l
        return count

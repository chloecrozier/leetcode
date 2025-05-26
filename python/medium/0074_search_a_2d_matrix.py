# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        left = 0
        right = len(m) * len(m[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            r = mid // len(m[0])
            c = mid % len(m[0])

            if m[r][c] == target:
                return True
            elif m[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

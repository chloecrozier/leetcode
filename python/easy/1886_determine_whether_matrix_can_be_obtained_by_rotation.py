# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/?envType=daily-question&envId=2026-03-22
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        for i in range(3):
            mat = list(zip(*mat[::-1]))

            mismatch = 0
            for r in range(len(target)):
                for c in range(len(target[r])):
                    if target[r][c] != mat[r][c]:
                        mismatch += 1
            if mismatch == 0:
                return True  

        return False

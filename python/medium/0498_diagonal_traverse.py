# https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        up = True
        row = 0
        col = 0
        prevR = 0
        prevC = 0
        height = len(mat)
        length = len(mat[0])

        while len(res) < (height * length):
            if up:
                while row >= 0 and col < length:
                    prevR = row
                    prevC = col
                    res.append(mat[row][col])
                    row -= 1
                    col += 1

                row = prevR
                col = prevC

                if col == length - 1:
                    row += 1
                else:
                    col += 1
                up = False
            else:
                while (row < height and col >= 0):
                    prevR = row
                    prevC = col
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                row = prevR
                col = prevC

                if row == height - 1:
                    col += 1
                else:
                    row += 1
                up = True
        return res

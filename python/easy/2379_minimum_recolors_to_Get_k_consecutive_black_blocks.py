# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/submissions/1568608859/?envType=daily-question&envId=2025-03-08
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        maxCount = 0
        countW = 0
        countB = 0
        for i in range(len(blocks) + 1):
            if i < len(blocks):
                if blocks[i] == 'W':
                    countW += 1
                else:
                    countB += 1
                if countW + countB > k:
                    if blocks[i - k] == 'W':
                        countW -= 1
                    else:
                        countB -= 1
            maxCount = max(maxCount, countB)
        return k - maxCount

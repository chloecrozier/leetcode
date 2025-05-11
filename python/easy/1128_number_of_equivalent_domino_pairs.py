# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        count = 0
        for tile in dominoes:
            if tile[0] > tile[1]:
                tile = (tile[1], tile[0])
            else:
                tile = (tile[0], tile[1])

            if tile in m:
                count += m[tile]
                m[tile] += 1
            else:
                m[tile] = 1
        return count

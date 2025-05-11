class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        for tile in dominoes:
            if tile not in m:
                if [tile[1], tile[0]] not in m:
                    m[tile[1], tile[0]] = 1
                else:
                    m[tile] = 1
        return len(m.values())

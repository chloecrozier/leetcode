# https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        m = {}
        res = 0
        for ans in answers:
            if ans in m:
                m[ans] += 1
            else:
                m[ans] = 1

        for key, value in m.items():
            res += (ceil(value / (key + 1))) * ((key + 1))

        return res

# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/?envType=daily-question&envId=2024-10-04
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sum = skill[0] + skill[len(skill) - 1]
        chemistry = skill[0] * skill[len(skill) - 1]
        i = 1
        j = len(skill) - 2

        while i < j:
            if sum != skill[i] + skill[j]:
                return -1
            else:
                chemistry += skill[i] * skill[j]
                i += 1
                j -= 1
        return chemistry

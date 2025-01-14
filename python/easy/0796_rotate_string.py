# https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2025-01-14
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True

        return goal in (s + s)

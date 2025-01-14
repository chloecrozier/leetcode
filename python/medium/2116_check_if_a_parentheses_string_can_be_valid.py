# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-12
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        openSeen = []
        unlockedSeen = []

        for i in range(len(s)):
            if locked[i] == '0':
                unlockedSeen.append(i)
            elif s[i] == '(':
                openSeen.append(i)
            else:
                if openSeen:
                    openSeen.pop()
                elif unlockedSeen:
                    unlockedSeen.pop()
                else:
                    return False

        while openSeen and unlockedSeen and openSeen[-1] < unlockedSeen[-1]:
            openSeen.pop()
            unlockedSeen.pop()

        return len(openSeen) == 0

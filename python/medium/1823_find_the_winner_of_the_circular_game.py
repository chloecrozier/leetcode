# https://leetcode.com/problems/find-the-winner-of-the-circular-game/?envType=problem-list-v2&envId=recursion
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        else:
            circle = [x for x in range(1, n + 1)]
            curr = 0
            while len(circle) > 1:
                curr = (curr + (k - 1)) % len(circle)
                del circle[curr]

            return circle[0] 

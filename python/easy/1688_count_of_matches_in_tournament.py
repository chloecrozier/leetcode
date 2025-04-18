# https://leetcode.com/problems/count-of-matches-in-tournament/description/
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2:
                n //= 2
                count += n + 1
            else:
                n /= 2
                count += n
        return int(count)

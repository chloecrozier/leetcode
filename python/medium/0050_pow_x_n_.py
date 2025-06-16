# https://leetcode.com/problems/powx-n/description/?envType=problem-list-v2&envId=recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            if n == 1:
                return x
            else:
                if n % 2:
                    half = self.myPow(x, (n - 1) // 2)
                    return x * half * half
                else:
                    half = self.myPow(x, n // 2)
                    return half * half
        elif n < 0:
            return 1 / self.myPow(x, abs(n))
        else:
            return 1

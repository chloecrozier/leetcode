# https://leetcode.com/problems/fibonacci-number/description/?envType=problem-list-v2&envId=recursion
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            prev = 0
            curr = 1
            for i in range(2, n + 1):
                temp = curr
                curr += prev
                prev = temp
            return curr

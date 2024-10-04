# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        sets = {'(': ')', '{': '}', '[': ']'}
        open = 0
        closed = 0
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if len(stack) == 0:
                    return False
                if sets[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        return True

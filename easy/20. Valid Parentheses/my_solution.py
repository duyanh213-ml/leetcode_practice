class Solution:
    def isValid(self, s: str) -> bool:
        opens = ('(', '[', '{')
        closes = (')', ']', '}')

        stack = []

        for char in s:
            if char in opens:
                stack.append(opens.index(char))
            elif stack == []:
                return False
            elif stack[-1] == closes.index(char):
                stack.pop()
            else:
                return False
        return stack == []

#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # myList = [
        #     ['(', ')'],
        #     ['{', '}'],
        #     ['[', ']'],
        # ]
        myStack = []
        for c in s:
            if c in ['(', '{', '[']:
                myStack.append(c)
            elif c == ')':
                if myStack and myStack[-1] == '(':
                    myStack.pop()
                else: return False
            elif c == ']':
                if myStack and myStack[-1] == '[':
                    myStack.pop()
                else: return False
            elif c == '}':
                if myStack and myStack[-1] == '{':
                    myStack.pop()
                else: return False
        return len(myStack) == 0


# @lc code=end


#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # if n == 1:
        #     return 1
        # myset = set()
        # res = 0
        # for i in range(n-1):
        #     myset = set()
        #     for j in range(i,n):
        #         if s[j] in myset:
        #             break
        #         myset.add(s[j])
        #         res = max(res, j - i + 1)
        # return res

        n = len(s)
        myDict = {}
        for i in range(256):
            myDict[chr(i)] = -1
        l = 0
        r = 0
        maxlen = 0
        while r < n:
            if myDict[s[r]] != -1:
                if myDict[s[r]] >= l:
                    l = myDict[s[r]] + 1
            length = r - l + 1
            maxlen = max(maxlen, length)
            myDict[s[r]] = r
            r += 1
        return maxlen

# @lc code=end


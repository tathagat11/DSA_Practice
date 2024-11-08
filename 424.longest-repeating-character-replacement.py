#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maxlen = 0
        # n = len(s)

        # for i in range(n):
        #     my_dict = {}
        #     max_count = 0
        #     for j in range(i, n):
        #         my_dict[s[j]] = my_dict.get(s[j], 0) + 1
        #         max_count = max(max_count, my_dict[s[j]])
        #         updates = j - i + 1 - max_count
        #         if updates <= k:
        #             maxlen = max(maxlen, j - i + 1)
        #         else: break
        
        maxlen = 0
        maxf = 0
        n = len(s)
        l = 0
        r = 0
        hm = {}
        for i in range(26):
            hm[i] = 0
        
        while r < n:
            hm[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, hm[ord(s[r]) - ord('A')])

            if r - l + 1 - maxf > k:
                hm[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            if r - l + 1 - maxf <= k:
                maxlen = max(maxlen, r - l + 1)
            
            r += 1

        return maxlen
# @lc code=end


#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        my_dict = {
            'a': -1,
            'b': -1,
            'c': -1,
            }
        r = 0
        while r < n:
            my_dict[s[r]] = r
            
            if my_dict['a'] != -1 and my_dict['b'] != -1 and my_dict['c'] != -1:
                count += 1 + min(my_dict['a'], my_dict['b'], my_dict['c'])
            
            r += 1
        return count
  
# @lc code=end


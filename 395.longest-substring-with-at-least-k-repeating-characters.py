#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxlen = 0
        n = len(s)
        
        for i in range(n):
            freq = {}
            
            for j in range(i, n):
                
                freq[s[j]] = freq.get(s[j], 0) + 1
                
                valid = True
                
                for char in freq:
                    if freq[char] < k:
                        valid = False
                        break
                
                if valid:
                    maxlen = max(maxlen, j - i + 1)
                    
        return maxlen

# @lc code=end

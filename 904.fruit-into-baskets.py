#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxlen = 0
        l = 0
        r = 0
        n = len(fruits)
        my_dict = {}
        while r < n:
            my_dict[fruits[r]] = my_dict.get(fruits[r], 0) + 1

            if len(my_dict) <= 2:
                maxlen = max(maxlen, r - l + 1)
            
            if len(my_dict) > 2:
                my_dict[fruits[l]] -= 1
                if my_dict[fruits[l]] == 0:
                    del my_dict[fruits[l]]
                l += 1
            
            r += 1
        
        return maxlen
                    

# @lc code=end


#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s = 0
        cur1s = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur1s += 1
                # print(f"At {nums[i]}:", cur1s)
            if nums[i] == 0:
                max1s = max(cur1s, max1s)
                cur1s = 0
        max1s =max(max1s, cur1s)
        return max1s
        
# @lc code=end


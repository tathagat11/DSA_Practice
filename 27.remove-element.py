#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

# @lc code=end


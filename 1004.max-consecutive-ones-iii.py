#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # O(n^2) solution (brute force)
        # n = len(nums)
        # maxlen = 0
        # for i in range(n):
        #     num0s = 0
        #     for j in range(i, n):
        #         if nums[j] == 0:
        #             num0s += 1
        #         if num0s <= k:
        #             maxlen = max(maxlen, j-i+1)
        #         else:
        #             break
        # return maxlen
        
        # Sliding window solution
        n = len(nums)
        maxlen = 0
        l = 0
        r = 0
        zeros = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen
# @lc code=end


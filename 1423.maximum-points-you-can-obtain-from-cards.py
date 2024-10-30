#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # res = 0
        # for i in range(k + 1):
        #     lsum = 0
        #     rsum = 0
        #     for j in range(i):
        #         lsum += cardPoints[j]
            
        #     for j in range(k - i):
        #         rsum += cardPoints[len(cardPoints)-1-j]
        #     this_sum = lsum + rsum
        #     res = max(this_sum, res)
        # return res
        lsum = 0
        rsum = 0
        maxsum = 0
        lsum = sum(cardPoints[:k])
        maxsum = lsum

        right = len(cardPoints) - 1

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[right]
            right -= 1
            maxsum = max(maxsum, lsum + rsum)

        return maxsum

# @lc code=end


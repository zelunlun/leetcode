import math

class Solution:
    def maxSubArray(self, nums):
        # dp = [[0]*len(nums) for i in range(2)]
        return math.inf * 0
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = Solution()
    print(ans.maxSubArray(nums))
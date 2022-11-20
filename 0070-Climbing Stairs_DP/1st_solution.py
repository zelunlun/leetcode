class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2: return n     # why I use this line and I get Correct answer?
                                # and Why I don't than get the Error message
        dp = [0]*(n+1)
        print(f'The basic dp is {dp}')
        dp[1] = 1
        dp[2] = 2               # <- List index assignment out of range?
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
""" Time Complexity: 

    Label: Dynamic Programming
"""

"""
    Explain -> Use fibonacci [0, 1, 2, 3, 5, 8, ...]
               than return DP[n]
    But how do we know that we can use fibonacci to
    solve this question 
"""

if __name__ == '__main__':
    ans = Solution()
    ans.climbStairs(2)
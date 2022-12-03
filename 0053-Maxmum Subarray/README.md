#### 這題是Middum的第一題，紀念一下  
#### 此題目前記錄三種解法  
> Label: Divide and Conquer, Dynamic Programming
  
* #### Force  
> skip

* #### Dynamic Programming  
    > Time Complexity : O(N), we are just iterating over the nums array once to compute the dp array and once more over the dp at the end to find maximum subarray sum. Thus overall time complexity is O(N) + O(N) = O(N)  
    > Space Complexity : O(N), for maintaining dp.  
    * ##### 1st 製表格  
    ```python
    class Solution:
        def maxSubArray(self, nums):
            dp = [[0]*len(nums) for i in range(2)]
            dp[0][0], dp[1][0] = nums[0], nums[0]
            for i in range(1, len(nums)):
                dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
                dp[0][i] = max(dp[0][i-1], dp[1][i])
            return dp[0][-1]
    ```  
    * ##### 2nd 製表格  
    ```python
    class Solution:
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
    ```
    →目前用這種,我覺得這個和`nums[i]`的比較 可以抽像想成爬山，前面遇到的正數相當於上山，一旦開始下山 如果不走到坑里是ok的，但加上下一個數總和為負數，就好比走到坑里去了，那麼完全可以丟掉，要嗎用以前的max 或者從新開始爬（reset 成0）

* #### Kadane's Algorithm 
> Time Complexity : O(N), for iterating over nums once  
> Space Complexity : O(1), only constant extra space is being used.
```python
class Solution:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
```



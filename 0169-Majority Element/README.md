* ### <span class='blue'>別人用的，更好的演算法</span>－^Time-Complexity：O(n)、Space-Complexity：^<span class='red'>^O(1)^</span>
    * 摩爾投票算法－Boyer–Moore Majority Vote Algorithm ^Time Complexity－O(n)、Space Complexity－O(1)^
```python=
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```
:::info
**筆記**：
核心思想為若是有人投A，另一個投票給B（在總投票人數 > 2的情況下）
那麼少了這兩個人的投票，對最後選舉的結果不會有影響
在已經給陣列的情況下可以利用，==不會在動到空間==
:::
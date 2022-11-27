## This qusestion have two solution  
Label: **`TwoPointer`**、**`Stack`**

### 1. Stack  
    > Time Complexity: **O( m + n )**  
    > Space Complexity: **O( m + n )**
```python  
class Solution:
    def backspaceCompare(self, S, T):
        l1 = self.stack(S, [])
        l2 = self.stack(T, [])
        return l1 == l2
        
    
    def stack(self, S, stack):
        for char in S:
            if char is not "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack
```  
  
### 2. Two Pointer
    > Time Complexity: **O( n )**  
    > Space Complexity: **O(1)**  
    > 類型：由右往左Index  

```python
class Solution(object):
    def backspaceCompare(self, S1, S2):
        r1 = len(S1) - 1 
        r2 = len (S2) - 1
        
        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(S1, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(S2, r2)
            if char1 != char2:
                return False
        return True
        
    
    def getChar(self, s , r):
        char, count = '', 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r
```

#### 參考:https://leetcode.com/problems/backspace-string-compare/discuss/145786/Python-tm
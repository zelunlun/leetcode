### This question have three solution :  
  
* ### 1. Use Hash  
    > This is my solution
* ### 2. Use Sorting  
```python
    l =  len(nums)
    if l < 2:
        return False
    nums.sort()
    for i in range(l-1):
        if nums[i] == nums[i+1]:
            return True
    return False
```
* ### 3. Use Set  
    > This is more concise  
```python
    numsSet =  set(nums)
    if len(nums) == len(numsSet):
        return False
    return True
```
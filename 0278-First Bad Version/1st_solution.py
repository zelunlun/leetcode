class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        while right>=left:
            middle = (left + right)//2
            if isBadVersion(middle) == True:
                right = middle - 1
            else:
                left = middle + 1
                result = left
        return result
    
""" Time Complex is O(log n), Space Complex is ?

    Label : Binary Search, Interactive
""" 



# class Solution:
#     def __init__(self):
#         self._list = []
#         self.left = None
#         self.right = None
    
#     def firstBadVersion(self, n: int) -> int:
#         if n == 1 :
#             return 1
#         for i in range(1,n+1):
#             self._list.append(i)
#         head = 0
#         tail = len(self._list)
#         average = (head + tail) // 2
#         if self._list[tail]:   
#             while self._list[tail] - self._list[head] > 2:
#                 if isBadVersion(self._list[average]) == True:  
#                         #   <-- default have isBadVersion() function
#                     tail = average - 1
#                 else:
#                     head = average + 1
#         return self._list(average)



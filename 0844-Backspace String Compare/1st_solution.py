# class Solution:
#     def backspaceCompare(self, S, T):
#         result_S = self.stack(S, [])
#         result_T = self.stack(T, [])
#         return result_S == result_T

#     def stack(self, S, stack):
#         for char in S:
#             if char != "#":
#                 stack.append(char)
#             else:
#                 if not stack:
#                     continue
#                 stack.pop()
#         return stack
class Solution(object):
    def backspaceCompare(self, S1, S2):
        r1 = len(S1) - 1 
        r2 = len (S2) - 1
        
        while r1 >= 0 or r2 >= 0:  # <- here is to count if s,t is finish counting
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

import math

if __name__ == "__main__":
    ans = Solution()
    result = ans.backspaceCompare("xywrrmp","xywrrm#p")
    # print(result)
    print(type(math.inf))    


"""
    自己的解法 -> 成功 , 希望在更快一點
    O(m+n) Time Complexity, O(1) Space Complexity
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        diction = {}
        for i in magazine:
            if i in diction:
                diction[i] += 1
            else:
                diction[i] = 1
        for eng in ransomNote:
            if eng in diction:
                diction[eng] -= 1
            else:
                return False
        for n in diction.values():
            if n < 0:
                return False
        return True

"""
    別人的解法
    據他說是O(n)
"""

""" Hey Leets! I have approached this problem using python dictionary (hashmap in other languages). 
First of all I have counted each letter in magazine and stored it in magDict. 
Now we will iterate through each character of ransomNote and if the character is present in dictionary 
then we will decrement that character from dictionary. If there are any character in ransomNote that is not present in magDict 
then we will return False. Otherwise return True."""

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         magDict = {}
#         for i in magazine:
#             if i in magDict:
#                 magDict[i] +=1
#             else:
#                 magDict[i] = 1
#         for j in ransomNote:
#             if magDict.get(j) and magDict[j]>0:
#                 magDict[j] -=1
#             else:
#                 return False
#         return True




"""
    1st-測試
"""

if __name__ == '__main__':
    ans = Solution()
    print(ans.canConstruct('aa','ab'))
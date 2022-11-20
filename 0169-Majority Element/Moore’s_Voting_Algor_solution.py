"""
    Time Complexity:    O(n)
    Space Complexity:   O(1)
    Relation Topic: Hash Table, Sorting, Divide and Conquer
    目前看不懂
"""

class Solution(object):
    def majorityElement(self, nums):
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol
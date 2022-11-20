"""
    Time Complexity:    O(n)
    Space Complexity:   O(n)
    Relation Topic: Hash Table, Sorting, Divide and Conquer

"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        average_len = len(nums) // 2
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num, times in count.items():
            if times > average_len:
                return num

if __name__ == '__main__':
    ans = Solution()
    answer = ans.majorityElement([2,2,1,1,1,2,2])
    print(answer)
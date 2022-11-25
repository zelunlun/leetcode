class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        l =  len(nums)
        if l < 2:
            return False
        nums.sort()
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == '__main__':
    ans = Solution()
    result = ans.containsDuplicate([2,14,18,22,22])
    print(result)
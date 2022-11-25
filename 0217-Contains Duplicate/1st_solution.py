class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        _dict = {}
        for num in nums:
            if num not in _dict:
                _dict[num] = 1
            else:
                _dict[num] += 1
        for i  in _dict.values():
            if i > 1:
                return True    
        return False

if __name__ == '__main__':
    ans = Solution()
    h = ans.containsDuplicate([2,14,18,22,22])
    print(h)

    
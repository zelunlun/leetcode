"""
    Time Complexity : O(max(M, N)), M & N is the length of string a, b;
    Space Complexity : O(max(M, N))
    Relative Topic: String
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0 : sum += ord(a[i]) - ord('0') # ord is use to get value of ASCII character
            if j >= 0 : sum += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sum > 1 else 0
            res += str(sum % 2)
        print(f'This is carry: {carry}')
        if carry != 0 : res += str(carry)
        return res[::-1]


if __name__ == '__main__':
    ans = Solution()
    answer = ans.addBinary("11","1")
    print(answer)
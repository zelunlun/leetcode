"""
    Time Complexity: ?
    Time Complexity: ?

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_two = int(a, 2)
        b_two = int(b, 2)
        sum_two = bin(a_two + b_two)
        sum_two = sum_two[2:]
        return sum_two



if __name__ == '__main__':
    ans = Solution()
    answer = ans.addBinary("11","1")
    print(answer)
class Solution:
    def backspaceCompare(self, S, T):
        result_S = self.stack(S, [])
        result_T = self.stack(T, [])
        return result_S == result_T

    def stack(self, S, stack):
        for char in S:
            if char != "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack


if __name__ == "__main__":
    ans = Solution()
    result = ans.backspaceCompare("ab###", "c#d##")
    print(result)
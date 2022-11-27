class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        behind = 0
        forward = 1
        forward_stack = []
        behind_stack = []
        t_stack = []
        s = s + "0"
        while behind < len(s):
            # print(s[behind]
            if s[forward] == '0':
                break
            if s[forward] == '#':
                forward_stack.append(s[behind])
            else:
                behind_stack.append(s[forward])
            behind += 1
            forward += 1
        
        return forward_stack[:], behind_stack[:]


if __name__ == "__main__":
    ans = Solution()
    result = ans.backspaceCompare("ab#c", "ad#c")
    print(result)
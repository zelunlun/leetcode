class Solution:
    def romanToInt(self, s: str) -> int:
        result, prev = 0, 0
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000 }
        for word in s[::-1]:
            if roman[word] >= prev:
                result += roman[word]
            else:
                result -= roman[word]
            prev = roman[word]
        return result
        
        # res, prev = 0, 0
        # dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # for i in s[::-1]:          # rev the s
        #     if dict[i] >= prev:    # prev = dict[i] 's times
        #         res += dict[i]     # sum the value if previous value same or more
        #     else:
        #         res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
        #     prev = dict[i]
        # return res

"""
    This way I couldn't know why have to add roman[s[-1]]
"""
        # roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}  
        # z = 0  
        # for i in range(0, len(s)-1):  
        #     if roman[s[i]] < roman[s[i+1]]:  
        #         z -= roman[s[i]]  
        #     else:  
        #         z += roman[s[i]]  
        # return z + roman[s[-1]]
"""
    This is my origin way, too bad
"""
        # roman = {
        #     "I":1,
        #     "V":5,
        #     "X":10,
        #     "L":50,
        #     "C":100,
        #     "D":500,
        #     "M":1000 }
        # _dict = {}
        # sum = 0
        # for word in s :
        #     if word not in _dict:
        #         _dict[word] = 1
        #     else:
        #         _dict[word] += 1
        # for word ,word_times in _dict.items():
        #     sum += roman[word] * word_times
        # for i in range(0, len(s)-1):
        #     if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X") :
        #         sum -= 1
        #     if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X") :
        #         sum -= 10
        #     if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X") : 
        #         sum -= 100
        # return sum


if __name__ == "__main__":
    ans = Solution()
    print(ans.romanToInt("IV")) 
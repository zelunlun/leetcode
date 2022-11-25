### Here have three different way to slove this question

* ### 1.  
    > This solution I have to understand it.
```python
def romanToInt(self, s: str) -> int:
	res, prev = 0, 0  
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}  
	for i in s[::-1]:          # rev the s  
		if dict[i] >= prev:  
			res += dict[i]     # sum the value iff previous value same or more  
		else:  
			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
		prev = dict[i]  
	return res  
```  
* ### 2.  
```python  
def romanToInt(self, s):  
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}  
    z = 0  
    for i in range(len(s)):  
        if roman[s[i]] < roman[s[i+1]]:  
            z -= roman[s[i]]  
        else:  
            z += roman[s[i]]  
    return z 
```  
* ### 3.  
    > This is the smartest ,But need to remember str.replace() 
```python  
class Solution:  
    def romanToInt(self, s: str) -> int:  
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0  
        s = s.replace("IV", "IIII").replace("IX", "VIIII")  
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")  
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")  
        for char in s:  
            number += translations[char]  
        return number  
```  

### 之後這題要再補個.gif
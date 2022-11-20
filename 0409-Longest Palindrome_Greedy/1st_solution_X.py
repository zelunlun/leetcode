"""
    Time Complexity:  O(n) Maybe
    Space Complexity: O(?)
    Relative Topic:  Hash Table, Greedy
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = []
        odd= 0
        for word in s:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        for times in count.values():
            ans.append(times)
            if times % 2 != 0:
                odd += 1
        if odd != 0:
            return sum(ans) - odd + 1        
        elif odd == 0:
            return sum(ans) - odd


if __name__ == '__main__':
    ans = Solution()
    test = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    answer = ans.longestPalindrome(test)
    
    print(answer)
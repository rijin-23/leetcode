class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) ==  1:
            return True
        res = ''
        for ch in s:
            if (ord(ch.lower()) > 47 and ord(ch.lower()) < 58) or (ord(ch.lower()) > 96 and ord(ch.lower()) < 123):
                res += ch.lower()
        if res == res[::-1]:
            return True
        else:
            return False
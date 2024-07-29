class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ''
        split_s = s.split(' ')
        print(split_s)
        i = len(split_s) - 1
        while i > -1:
            if len(split_s[i]) != 0:
                new_s += split_s[i] + ' '
                i -= 1
            else:
                i-=1
        return new_s[:-1]
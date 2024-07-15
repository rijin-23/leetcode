class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = 0
        counter = 0
        i = len(s)-1
        while i > -1:
            if s[i] == ' ' and flag == 0:
                i-=1
            elif s[i] == ' ' and flag == 1:
                return counter
            else:
                flag = 1
                counter+=1
                i-=1
                if i == -1:
                    return counter
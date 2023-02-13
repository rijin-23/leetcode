class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary={}
        keyVal = []
        if len(s) != len(t):
            return(False)
        for x in range(len(s)):
            keyVal.append((s[x],t[x]))
        for key,value in keyVal:
            if key not in dictionary and value not in dictionary.values():
                dictionary[key] = value
        res = ""
        for x in s:
            if x not in dictionary:
                return False
            res = res + dictionary[x]
        if res == t:
            return(True)
        else:
            return False
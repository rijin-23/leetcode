class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch_dict = {}
        traversed = {}
        for index,ch in enumerate(s):
            if ch not in ch_dict and t[index] not in traversed:
                ch_dict[ch] = t[index]
                traversed[t[index]] = 1
            elif t[index] in traversed and ch not in ch_dict:
                return False
            else:
                if ch_dict[ch] != t[index]:
                    return False
        return True
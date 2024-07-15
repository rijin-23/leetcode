class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_count_s = {}
        ch_count_t = {}
        if len(s) != len(t):
            return False
        for index, value in enumerate(s):
            if value not in ch_count_s:
                ch_count_s[value] = 1
            else:
                ch_count_s[value] += 1
            if t[index] not in ch_count_t:
                ch_count_t[t[index]] = 1
            else:
                ch_count_t[t[index]] += 1

        for key in ch_count_s:
            if key not in ch_count_t:
                return False
            else:
                if ch_count_s[key] != ch_count_t[key]:
                    return False
        return True

            
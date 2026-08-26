class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        if len(t) == len(s):
            for i in range(len(s)):
                count_s[s[i]] = count_s.get(s[i], 0) + 1
                count_t[t[i]] = count_t.get(t[i], 0) + 1
            return count_t == count_s
        return False

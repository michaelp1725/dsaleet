class Solution(object):
    def isAnagram(self, s, t):
        freq = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
        for j in range(len(s)):
            if t[j] not in freq:
                return False
            else:
                freq[t[j]] -= 1
            if freq[t[j]] == 0:
                del freq[t[j]]
        return True
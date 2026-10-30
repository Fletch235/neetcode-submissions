class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        di = {}
        for i in range(len(s)):
            di[s[i]] = di.get(s[i], 0) + 1
            di[t[i]] = di.get(t[i], 0) - 1


        for i in di:
            print(di[i])
            if di[i] != 0:
                return False
        return True
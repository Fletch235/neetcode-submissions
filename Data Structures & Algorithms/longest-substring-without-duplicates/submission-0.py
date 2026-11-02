class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)

        if s == "":
            return 0

        seen = set()
        current = 0
        best = 0
        for i in range(N):
            while s[i] in seen:
                seen.remove(s[i - current])
                current -= 1
            seen.add(s[i])
            current += 1
            if current > best:
                best = current

            
        return best
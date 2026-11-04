class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        charset = set(s)

        for char in charset:
            l = 0
            count = 0

            for r in range(len(s)):
                if s[r] == char:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                result = max(result, r - l + 1)
        
        return result
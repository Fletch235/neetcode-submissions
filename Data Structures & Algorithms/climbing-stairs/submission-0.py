class Solution:
    def climbStairs(self, n: int) -> int:
        out = 1
        j = 0
        for i in range(n):
            prev = out
            out += j
            j = prev
        return out
    
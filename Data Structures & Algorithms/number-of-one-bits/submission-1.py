class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        for i in range(30, -1, -1):
            power = 2 ** i
            if n >= power:
                out += 1
                n -= power
        
        return out
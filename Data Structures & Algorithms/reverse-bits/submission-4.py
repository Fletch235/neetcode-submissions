class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            b = (n >> i) & 1
            out += (b << (31 - i))
        return out

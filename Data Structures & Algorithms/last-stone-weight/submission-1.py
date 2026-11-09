import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()
            if not stone1 == stone2:
                bisect.insort(stones, max(stone1-stone2, stone2-stone1))
        if stones:
            return stones[0]
        return 0

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        out = [0] * (n + 1)
        for i in range(2, n + 1):
            out[i] = min(out[i - 1] + cost[i - 1], out[i - 2] + cost[i - 2])

        return out[n]
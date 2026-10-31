class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [0] * N
        best = 101 # 0 <= prices[i] <= 100

        for i in range(N):
            dp[i] = max(0, prices[i] - best)
            if prices[i] < best:
                best = prices[i]
        return max(dp)
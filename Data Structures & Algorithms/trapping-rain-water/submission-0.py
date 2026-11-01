class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        left = [0] * N
        for i in range(1, N):
            left[i] = max(height[i-1], left[i-1])

        right = [0] * N
        for i in range(N - 2, -1, -1):
            right[i] = max(height[i+1], right[i+1])

        water = 0
        for i in range(N):
            water += max(min(left[i], right[i]) - height[i], 0)
        return water
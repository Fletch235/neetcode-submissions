class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)

        left = 0
        right = N - 1
        best = 0
        while left < right:
            candidate = min(heights[left], heights[right]) * (right - left)
            if candidate > best:
                best = candidate
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best
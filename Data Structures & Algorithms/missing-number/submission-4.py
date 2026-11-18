class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        if nums[0] <= 0:
            return nums[n-1] + 1
        else:
            return nums[0] - 1
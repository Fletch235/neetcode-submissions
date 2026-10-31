class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 0
                curr = num
                while curr in nums_set:
                    streak += 1
                    curr += 1
                res = max(res, streak)
                
        return res
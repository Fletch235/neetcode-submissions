class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
            
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False
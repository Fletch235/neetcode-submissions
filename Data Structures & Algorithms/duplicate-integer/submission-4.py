class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Brute:
        #for i in range(0, len(nums)):
        #    for j in range(0, len(nums)):
        #        if nums[i] == nums[j] and i != j:
        #            return True
        #return False

        #
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
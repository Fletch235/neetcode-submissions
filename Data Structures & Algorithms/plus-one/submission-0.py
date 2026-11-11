class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(digits)
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
            if i == 0:
                out = [1]
                out.extend(digits)
                return out
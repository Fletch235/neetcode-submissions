class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int) #key: int      value: int amount of instances

        for num in nums:
            numdict[num] += 1

        out = []
        for i in range(k):
            best = max(numdict.items(), key = lambda item: item[1])[0]
            out.append(best)
            numdict.pop(best)
        return out
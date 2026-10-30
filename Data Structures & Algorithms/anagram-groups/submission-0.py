from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        hashmap = {}#key: sorted string, value: index

        output = defaultdict(list)

        for string in strs:

            
            sort = "".join(sorted(string))
            output[sort].append(string)
        return list(output.values())
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = []
        for item in strs:
            sizes.append(str(len(item)))
            sizes.append(",")
        sizes.append("#")
        sizes.extend(strs)
        return "".join(sizes)
    

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []

        lens = []
        i = 0
        while s[i] != "#":
            j = i
            while s[j] != ',':
                j += 1
            lens.append(int(s[i:j]))
            i = j + 1
        
        i += 1
        for size in lens:
            res.append(s[i:i+size])
            i += size
            
        return res

        

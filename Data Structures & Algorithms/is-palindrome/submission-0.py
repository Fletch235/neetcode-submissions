class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist = list(s)
        string = ""

        for item in slist:
            if item.isalnum():
                string = string + item

        string = string.lower()
        N = len(string)
        
        for i in range(N // 2):
            if string[i] != string[N-i-1]:
                return False

        return True
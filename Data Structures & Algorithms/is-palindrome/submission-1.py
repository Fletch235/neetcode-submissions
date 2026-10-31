class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist = list(s)
        alnum = ""

        for item in slist:
            if item.isalnum():
                alnum = alnum + item

        alnum = alnum.lower()
        N = len(alnum)

        for i in range(N // 2):
            if alnum[i] != alnum[N-i-1]:
                return False

        return True
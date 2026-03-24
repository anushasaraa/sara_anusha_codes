class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a:str, b:str) -> bool:
            n = len(a)
            l = 0
            r = n - 1
            while l < r and a[l] == b[r]:
                l += 1
                r -= 1
            t = a[l:r+1]
            p = b[l:r+1]
            return t == t[::-1] or p == p[::-1]
        return check(a,b) or check(b,a)

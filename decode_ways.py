class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev = s[0]
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] == '0':
                if prev not in '12':
                    return 0
                dp[i] = dp[i - 2]
            else:
                if prev not in '12' or (prev == '2' and s[i - 1] in '789'):
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            prev = s[i - 1]
        
        return dp[-1]

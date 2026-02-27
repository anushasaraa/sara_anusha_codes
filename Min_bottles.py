def solve():
    n = int(input())
    bottles = [2, 3, 5, 7, 11]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for b in bottles:
            if i >= b:
                dp[i] = min(dp[i], dp[i - b] + 1)
    
    print(dp[n])

solve()

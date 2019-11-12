dp = [[for i in range(10)] for j in range(1000)]
n = int(input())
summary = 0
for i in range(0, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][k]

for i in range(10):
    summary += dp[n][i]

print(summary % 10007)

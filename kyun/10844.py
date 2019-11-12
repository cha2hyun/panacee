n = int(input())
dp = [[0 for x in range(10)] for y in range(n)]
print(dp)

if n >= 1:
    for j in range(n):
        for i in range(10):
               dp[j][i] = 1
print(dp)

for i in range(1, n):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = j - 1
        if j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

sum = int(0)

for i in range(1,10):
    sum = sum + dp[n-1][i]

print(sum)
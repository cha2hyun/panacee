x = list()
dp = list()
n = int(input())

for i in range(0, n):
    x.append(int(input()))
    dp.append(0)

dp[0] = x[0]

test = x[0]

for k in range(1, n):
    dp[k] = max(x[k], dp[k - 1] + x[k])

    test = max(test, dp[k])


print(test)

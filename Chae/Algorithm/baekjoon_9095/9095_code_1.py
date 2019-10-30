# coding=utf-8
# 점화식 dp[n] = dp[n-3] + dp[n-2] + dp[n-1]
# 메모제이션 기법 때문에 배열에 선언하여 캐싱

memorize = [i for i in range(0, 11)]
memorize[0] = 0
memorize[1] = 1
memorize[2] = 2
memorize[3] = 4


def dp(n):
    if n < 4:
        return memorize[n]
    return dp(n - 3) + dp(n - 2) + dp(n - 1)


arr = []
k = int(input())
while k:
    arr.append(int(input()))
    k -= 1

flag = len(arr)
i = 0
while flag:
    print(dp(arr[i]))
    i += 1
    flag -= 1

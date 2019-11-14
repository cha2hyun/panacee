dp = []

n = int(input())

if n >= 1:
    for i in range(0, 10):
        dp.append(int(1))

for j in range(1, n):
    for i in range(0, 10):
        if i == 0:
            dp[i] = 1
        else:
            dp[i] = dp[i] + dp[i - 1]
sum = 0
int(sum)
for k in range(0, 10):
    sum = sum + dp[k]

print(sum % 10007)
# #include <stdio.h>
#
# int main() {
# 	int dp[10] = { 0 };
#
# 	int n;
# 	scanf_s("%d", &n);
#
# 	if (n == 1) {
# 		for (int i = 0; i < 10; i++) dp[i] = 1;
# 	}
#
# 	for (int i = 1; i <= n; i++) {
# 		for (int j = 0; j < 10; j++) {
# 			if (j == 0) {
# 				dp[j] = 1;
# 			}
# 			else {
# 				dp[j] += dp[j - 1];
# 			}
#
# 		}
# 	}
# 	for (int i = 0; i < 10; i++) printf("%d ", dp[i]);
# 	printf("\n");
#
# 	int sum = 0;
# 	for (int i = 0; i < 10; i++) {
# 		sum += dp[i];
# 	}
#
# 	printf("%d\n", sum );
#
# 	system("pause");
# }

# coding=utf-8
# 루트값임
import math

k = int(input())
n = []
for i in range(0, k):
    s = int(input())
    n.append(s)

for i in range(0, k):
    print(int(math.sqrt(n[i])))

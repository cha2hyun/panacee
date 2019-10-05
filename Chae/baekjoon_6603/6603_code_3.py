# -*- coding: utf-8 -*-
import itertools
S = []
K = []
flag = True

while flag:
    s = input().split()
    k = int(s.pop(0))

    if k < 6 or k != len(s):
        break

    temp = list(map(int, s))
    for i in temp:
        if i < 1 or i > 50:
            flag = False
    if not flag:
        break

    if k == 0:
        break

    S.append(s)
    K.append(k)


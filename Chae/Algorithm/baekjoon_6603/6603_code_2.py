# -*- coding: utf-8 -*-
# iterator.combinations 모듈 이용
# coding=utf-8
import itertools
S = []
K = []
flag = True

# 입력받으면서 예외처리 체크
while flag:
    s = input().split()
    k = int(s.pop(0))

    # 예외처리, 6보다 작거나 입력해야하는 수와 실제 입력받은수 확인
    if k < 6 or k != len(s):
        break

    # 예외처리, 정수형으로 변형해서 1부터 50인지 확인
    temp = list(map(int, s))
    for i in temp:
        if i < 1 or i > 50:
            flag = False
    if not flag:
        break

    # 탈출문 0 입력시 종료
    if k == 0:
        break

    S.append(s)
    K.append(k)

# 출력
flag = len(S)
i = 0
while flag:
    for S[i] in itertools.combinations(S[i], 6):
        print(" ".join(S[i]))
    print()
    i = i + 1

    # 탈출문
    if i == flag:
        break

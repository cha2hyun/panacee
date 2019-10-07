# 재귀 이용
# coding=utf-8
S = []
K = []
flag = True

# 입력받으면서 예외처리 체크
while flag:
    s = input().split()
    k = int(s.pop(0))

    # 예외처리
    if k < 6 or k != len(s):
        break

    # 예외처리
    temp = list(map(int, s))
    for i in temp:
        if i < 1 or i > 50:
            flag = False
    if not flag:
        break

    # 탈출문
    if k == 0:
        break

    S.append(s)
    K.append(k)

# 함수
def combination(k, available, used):
    if len(used) == k:
        yield tuple(used)
    elif len(available) == 0:
        pass
    else:
        head = available.pop(0)
        used.append(head)
        for c in combination(k, available[:], used[:]):
            yield c
        used.pop()
        for c in combination(k, available[:], used[:]):
            yield c

# 메인
Lotto_num = 6
for i in range(0, len(S)):
    print("")
    Result = [c for c in combination(Lotto_num, S[i], [])]
    for k in range (0, len(Result)):
        print(" ".join(Result[k]))
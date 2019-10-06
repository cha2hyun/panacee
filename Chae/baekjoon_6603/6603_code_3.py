# dfs 이용
# coding=utf-8
# S = []
# K = []
# flag = True
#
# # 입력받으면서 예외처리 체크
# while flag:
#     s = input().split()
#     k = int(s.pop(0))
#
#     # 예외처리
#     if k < 6 or k != len(s):
#         break
#
#     # 예외처리
#     temp = list(map(int, s))
#     for i in temp:
#         if i < 1 or i > 50:
#             flag = False
#     if not flag:
#         break
#
#     # 탈출문
#     if k == 0:
#         break
#
#     S.append(s)
#     K.append(k)

def comb1(n, available, used):
    if len(used) == n:
        yield tuple(used)
    elif len(available) == 0:
        pass
    else:
        head = available.pop(0)
        used.append(head)
        for c in comb1(n, available[:], used[:]):
            yield c
        used.pop()
        for c in comb1(n, available[:], used[:]):
            yield c


def comb2(n, available, used):
    if len(used) == n:
        yield tuple(used)
    elif len(available) == 0:
        pass
    else:
        for c1 in comb2(n, available[1:], used[:] + [available[0]]):
            yield c1
        for c1 in comb2(n, available[1:], used[:]):
            yield c1

temp1 = 'abc'
test = [c for c in comb1(2, list(temp1), [])]
print(test)
test1 = [c for c in comb2(2, list(temp1), [])]
print(test1)
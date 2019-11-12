# coding=utf-8
# 연습용
# itertools 모듈 사용
import itertools

# 입력받은것을 공백으로 구분하여 리스트 S에 저장한다.
S = input().split()

# S의 첫번째 요소를 pop 해서 K에 저장한다. pop 을 했기 때문에 리스트에서 삭제됨
K = int(S.pop(0))


# 예외처리 체크하는 변수선언
flag = True

# 예외처리 1
# 배열의 수가 6이하거나 K가 배열의 수랑 다르면 중지
if K < 6 or K != len(S): flag = False

# 예외처리 2
# 1 ~ 49 인지 확인
# 리스트 S 를 정수형으로 변환하여 Temp 에 저장하여 비교
Temp = list(map(int, S))
for i in Temp:
    if i < 1 or i > 50:
        flag = False

# 오류 없을때 실행
# 리스트 S 에 있는 원소들중 6개로 이루어진 조합을 출력
if flag:
    for S in itertools.combinations(S, 6):
        print(" ".join(S))


# 참고
# [python] itertools를 이용해 순열과 조합 구하기
# https://itholic.github.io/python-combination-permutation/
#
# import itertools
# arr = ['1', '2', '3']
# print("arrays -> ", arr)
# #순열방식 - permutations
# print()
# print("itertools.permutations(arr)")
# print(list(map(' '.join, itertools.permutations(arr))))
# print("itertools.permutations(arr, 2)")
# print(list(map(' '.join, itertools.permutations(arr, 2))))
# #조합방식 - combinations
# print()
# print("itertools.combinations(arr, 3)")
# print(list(map(' '.join, itertools.combinations(arr, 3))))
# print("itertools.combinations(arr, 2)")
# print(list(map(' '.join, itertools.combinations(arr, 2))))


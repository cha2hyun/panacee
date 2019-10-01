T = int(input("테스트 케이스 수 입력: "))

for i in range(0, T):
    N = int(input("배열의 크기: "))
    X = [int(input()) for j in range(N)]
    Max = X[0]
    result = X[0]
    for j in range(1, len(X)):
        Max = max(Max + X[j], X[j])
        result = max(Max, result)
    print(result)

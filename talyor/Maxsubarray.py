testcase = int(input('테스트케이스수 입력'))
Array = list()

for i in range(0, testcase) :
    N = int(input('배열의 크기 입력'))
    Array = [int(input('배열 입력')) for j in range(N)]
    print(Array)
    value = 0
    for x in range(0, N) :
        sum =0
        for y in range(x, N) :
            sum += Array[y]
            value = max(value, sum)
    print("최대합은?", value)
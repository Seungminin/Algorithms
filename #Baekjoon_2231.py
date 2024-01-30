#Baekjoon_2231 Solution
import sys
input = sys.stdin.readline

INF = 1000
#앞자리가 -1인 경우
def low_fir(N):
    sec = (10**length - 1) - 1
    boundary = N * (10 ** (length - 1)) + sec + N + sum(map(int,str(sec)))
    constructor = INF
    if boundary < num:
        return constructor
    elif boundary == num:
        constructor = (N+1)*(10**length-1)-1
    else:
        for i in range(10 ** (length - 1)):
            current_num = N * (10 ** (length - 1)) + i
            current_sum = current_num + sum(map(int, str(current_num)))
            if current_sum == num:
                constructor = min(constructor, current_num)

    return constructor

#앞자리가 arr[0]에 있는 수일 경우
def high_fir(N):
    constructor = INF
    for i in range(10**(length-1)):
        current_num = N * (10 ** (length - 1)) + i
        current_sum = current_num + sum(map(int, str(i))) + N
        if current_sum == num:
            constructor = min(constructor, current_num)
    return constructor

def sum_of_divisor():
    fir = int(arr[0])

    low_value=low_fir(fir-1)
    high_value=high_fir(fir)

    print(low_value)
    print(high_value)
    result = min(low_value,high_value)

    if result == INF:
        return 0
    else:
        return result

if __name__ == '__main__':
    arr = input().strip() #문자열 공백제거.
    num = int(arr)
    length = len(arr)
    res = sum_of_divisor()
    print(res)
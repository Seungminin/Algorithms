'''
#Baekjoon_10448 유레카 이론
#Tn 삼각수들의 값을 저장을 해두고 DP의 점화식을 이용해서 문제를 풀어야 한다.
#가장 큰 수를 빼서 다른 값들을 구하려고 노력하였다 -> Greedy처럼 문제를 풀었을 때 답이 나오지 않는다.

#T(100)이 가장 크다고 가정, Tn의 삼각수들을 저장.
INF = 100 
T = [0 for i in range(INF)] #삼각수들 저장
for i in range(1,INF):
    T[i] = i*(i+1)//2

def Eureka(n,times):
    count = 0
    low_n = n
    for k in range(3):
        for i in range(1,times+1):
            if(T[i] > low_n):
                index = i-1
                count+=1
                break
            elif(T[i]==low_n and count == 2):
                index = i
                count+=1
                break
            elif(T[i]==low_n and count != 2):
                index = i-1
                count+=1
                break
        #index는 n의 값을 가지고 있다.
        low_n = low_n-T[index]
        print("low_n :",low_n," T[index] : ",T[index], " index : ",index)
        times = index
    if low_n == 0:
        return 1
    return 0

N = int(input("Please type the number of n : "))
for i in range(N):
    n = int(input("Please type the number : "))
    print(Eureka(n,INF))
'''
MAX_N = 1000
dp = [0] * (MAX_N + 1)

# 삼각수 계산
triangular_numbers = []
i = 1
while True:
    triangular_number = i * (i + 1) // 2
    if triangular_number > MAX_N:
        break
    triangular_numbers.append(triangular_number)
    i += 1

# DP 테이블 갱신
for i in range(len(triangular_numbers)):
    for j in range(i, len(triangular_numbers)):
        for k in range(j, len(triangular_numbers)):
            total = triangular_numbers[i] + triangular_numbers[j] + triangular_numbers[k]
            if total <= MAX_N:
                dp[total] = 1

# 함수 정의
def Eureka(n):
    return dp[n]

# 입력 받기
N = int(input("Please type the number of test cases: "))
for _ in range(N):
    n = int(input("Please type the number: "))
    print(Eureka(n))

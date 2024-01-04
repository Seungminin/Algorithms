#Baekjoon_1149 Solution RGB 집 색칠하기 (Greedy_version, DP_version)

#Greedy Version
INF = 9999
'''
def Min_f(n):
    min = INF
    index = INF
    sum = 0
    for i in range(n):
        for j in range(n):
            if(min>arr[i][j] and j!=index): #가장 작은 값을 구하려고 하는 Greedy Algorithm
                min=arr[i][j]
                index = j
        sum+=min
        min = INF
    return sum

N = int(input("Please type N : "))
arr = [[0 for j in range (N)]for i in range (N)] #배열 2차원 선언  
for i in range(N):
    arr[i] = list(map(int, input().split())) #배열 입력하기, 한번에 띄어쓰기를 통해서 입력할 때 이용한다.
print("The small cost : ",Min_f(N)) '''

#DP Version 합한 결과를 가지고 내려온다. 
#DP에서는 minimal한 결과값들을 list, 배열에 저장을 하여 memorization을 한다.
import sys
n = int(sys.stdin.readline())
colors = [] #list를 선언하여 이차원 배열로도 사용할 수 있다.   
d = []

for i in range (n):
    r, g, b = list(map(int, sys.stdin.readline().split()))
    colors.append([r,g,b])
    d.append([INF, INF, INF]) #초기화 단계
    d[0][0] = colors[0][0]
    d[0][1] = colors[0][1]
    d[0][2] = colors[0][2]

for i in range(1,n):
    d[i][0] = min(d[i-1][1],d[i-1][2]) + colors[i][0]
    d[i][1] = min(d[i-1][0],d[i-1][2]) + colors[i][1]
    d[i][2] = min(d[i-1][0],d[i-1][1]) + colors[i][2]

res = min(d[n-1][0],d[n-1][1],d[n-1][2])
print(res)
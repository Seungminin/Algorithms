#Baekjoon_1699 Solution
import sys

def Find_min(n):
    for i in range(2,N+1):
        for j in range(2,i+1):
            if(i<j*j):
                continue
            d[i] = min(d[i], d[i-j*j]+1)
    return d[n]

N = int(sys.stdin.readline())
d = [i for i in range(N+1)] #배열을 선언해주고 초기화를 해준다. (list를 초기화)
#print(d)
print("The minimum :", Find_min(N), end = '')
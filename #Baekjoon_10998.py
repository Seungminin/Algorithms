#Baekjoon_10998 Solution
import sys
input = sys.stdin.readline

def find_DP():
    row = n - 1
    col = 0
    count = 0
    while True:
        if row == 0 and col ==n-1:
            if DP[row][col] == 1:
                count+=1
                break
            break
        if(DP[row][col]==1):
            count += 1
        row = row - 1
        col = col + 1
    
    if count == n:
        return 1
    else:
        return 0

def set_DP():
    for i in range(n):
        for j in range(n):
            if(input_str[i]==input_str[j]):
                DP[i][j] = 1
            else:
                DP[i][j] = 0
    print(DP)
    print(find_DP())
    
#python에서 String은 문자열 배열로 저장이 된다.
input_str = input()
n= len(input_str) - 1

DP = [[0 for _ in range(n)]for _ in range(n)]
set_DP()

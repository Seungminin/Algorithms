#Baekjoon_2579 Solution
import sys
#Greedy Algorithm -> 한계 : 만약 score가 같은 경우 규칙이 지켜지려면 뒤에 있는 Score가 어떤 지 알아야한다.
'''def Find_max(n):
    sum = 0
    index = 0
    sum+=stairs[index]
    print("index : ,Sum: ", index,sum)
    while 1:
        if(index==n-1):
            break
        elif(index == n-3):
            index+=2
            sum+=stairs[index]
            break
        elif(index == n-2):
            index+=1
            sum+=stairs[index]
            break
        if(stairs[index+1] >stairs[index+2]): #두 칸 이동하는 경우
            index +=1
            sum+=stairs[index]
            print("index : ,Sum: ", index,sum)
            index+=2
            sum+=stairs[index]
            print("index : ,Sum: ", index,sum)
        else:                                 #한 칸 이동하는 경우
            index+=2
            sum+=stairs[index]
            print("index : ,Sum: ", index,sum)
    return sum

N = int(sys.stdin.readline())
stairs = [0]*(N) #stairs list 설정, 초기화 후 입력
stairs = list(map(int, sys.stdin.readline().split())) #1차원 배열을 입력받을 때는 반복문을 사용하지 않는다.
#print(stairs)
print("The maximum : ", Find_max(N))'''

#DP Algorithm -> 계속 정보를 저장해서 이용하기.
def Find_max(n):
    count = 1
    DP[0] = stairs[0] #initialize DP[0]

    for i in range(n-1):
        if(i==n-2):
            DP[i+1] = max((DP[i] + stairs[i+1]),DP[i+1])
            break
        if(count == 2 and i != n-2):
            DP[i+2] = max((DP[i]+stairs[i+2]),(DP[i+1]+stairs[i+2]))
            count = 1
        else:
            DP[i+1] = max((DP[i] + stairs[i+1]),DP[i+1])
            count+=1
            DP[i+2] = max((DP[i] + stairs[i+2]),DP[i+2])
    print(DP)
    return DP[n-1]
N = int(sys.stdin.readline())
stairs = [0] * (N)
DP = [0] * (N) 
stairs = list(map(int,sys.stdin.readline().split()))
print("The Maximum : ", Find_max(N))
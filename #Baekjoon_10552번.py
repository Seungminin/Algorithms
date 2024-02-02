#Baekjoon_10552번 문제 DOM Solution
import queue
import sys
input = sys.stdin.readline

data_queue = queue.Queue()

def Find_change(person,channel):
    while True:
        index = float('inf')
        for i in range(N): #가장 나이가 어린 친구 찾기
            if person[i][1] == channel:
                if index>i:
                    index = i
        if index == float('inf'):
            return data_queue.qsize()
        
        data_queue.put(index)

        if data_queue.qsize()>N:
            return -1
        channel = person[index][0]

if __name__ == '__main__':
    N,M,P = map(int,input().split())

    #N x N 사람들 리스트 입력.
    person = [[0] * N for _ in range(N)]

    for i in range(N):
        row_data = list(map(int,input().split()))
        person[i] = row_data

    res = Find_change(person,P-1)

    print(res)
    '''defensive code.
    for i in person:
        for j in i:
            print(j, end = " ")
        print()'''
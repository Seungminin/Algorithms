#Baekjoon_1012번 Solution
#BFS방식으로 문제를 푼다.
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# x는 row, y는 column
def bfs(x,y):
    graph[y][x] = 0
    data.append((x,y)) #(x,y)
    #data라는 queue안에 parameter값들이 있을 때까지 즉 BFS에서 하나의 노드에서 갈 수 있는 모든 점들을
    #queue append를 하였고, 그 갈 수 있는 점들이 모두 확인 될 때까지.
    while data:
        x,y = data.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx]==1:
                data.append((nx,ny))
                graph[ny][nx] = 0

if __name__ == "__main__":
    T = int(input()) #Test case
    for _ in range(T):
        data = deque()
        count = 0
        M,N,K = map(int,input().split())
        graph = [[0]*M for _ in range(N)] #initialize
        for _ in range(K):
            x,y = map(int, input().split())
            graph[y][x] = 1

        for row in range(N):
            for col in range(M):
                if graph[row][col] == 1:
                    bfs(col,row) #x,y를 전달
                    count+=1
        print(count)
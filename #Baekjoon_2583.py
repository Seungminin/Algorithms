#Baekjoon_2583 Solution
#DFS버전, x,y라고 해서 가로, 세로라고 생각하지 말고 list에 들어가는 열로 생각하기. recursion하게 불러오가
import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)
input = sys.stdin.readline
#Update
dx = [-1, 1, 0, 0]
dy = [0 , 0, -1, 1]
count = 0

def DFS(x,y):
    global count
    if x<0 or x>=row or y<0 or y>=col:
        return 0
    if G[x][y] == 1:
        return 0
    
    #계산했던 공간은 1로 바꿔주기.
    G[x][y] = 1
    count+=1

    for i in range(4):
        DFS(x+dx[i],y+dy[i])

    return count

if __name__ =='__main__':
    #가로, 세로, 영역들 입력받기
    row, col, A = map(int, input().split())

    G = [[0]*(col) for _ in range(row)]

    for _ in range(A):
        x1, y1, x2, y2 = map(int,input().split())
        for i in range(y1,y2):
            for j in range(x1,x2):
                G[i][j] = 1
    
    for i in G:
        for j in i:
            print(j, end = ' ')
        print()
    
    res = []
    for i in range(row):
        for j in range(col):
            cnt = DFS(i,j)
            if cnt:
                res.append(cnt)
                count=0
    
    res.sort()
    print(len(res))
    for i in res:
        print(i, end = " ")
    
'''
#BFS버전, recursion하게 부르지 않고, 하나의 점에서 반복문을 통해서 펼쳐진다. 갈 수 있는 곳까지 넓게
from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(m - y1 - 1, m - y2 - 1, -1):
            graph[j][i] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global answer
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                size += 1
    result.append(size)

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i, j)
            
result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
'''
#5972번 문제 Solution, 최단 거리로 모든 노드들을 방문할 떄 가중치를 얼마나 가져가야 하는 지.
import sys
input = sys.stdin.readline
import queue

data_queue = queue.Queue() #queue를 이용하여 put, get method를 이용할 수 있다.

def choose(distance, found):
    min = float('inf')
    min_index = -1

    for i in range(N):
        if(distance[i]<min and found[i] ==0):
            min = distance[i]
            min_index = i
    return min_index

#Dijkstra algorithm을 이용하여 문제 풀기.
def shortest_path(Graph, start):
    distance = [float('inf')] * N
    found = [0] * N
    #start정점에서 시작되는 distance
    for i in range(N):
        distance[i] = Graph[start][i]
    found[start] = 1
    data_queue.put(start)

    #start정점에서 가장 짧은 weight를 가진 정점을 찾는다.
    for i in range(N-1):
        u = choose(distance,found)
        found[u] = 1
        data_queue.put(u)

        for j in range(N):
            if(distance[u]+Graph[u][j]<distance[j]):
                distance[j] = distance[u]+Graph[u][j]
        last_index = data_queue.get()
    return distance[last_index]

if __name__ =='__main__':
    # N은 node의 개수, M의 edge의 개수
    N,M = map(int,input().split())

    #인접행렬 초기화
    G = [[float('inf') for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i==j:
                G[i][j]=0
    #인접행렬 data입력
    for i in range(M):
        A,B,C = map(int,input().split())
        G[A-1][B-1] = C
        G[B-1][A-1] = C
    
    weight = shortest_path(G, 0)
    print(weight)
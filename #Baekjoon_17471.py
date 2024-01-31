'''#Baekjoon_17471 Solution
import sys
input = sys.stdin.readline

def Promising(index):
    new_A_list=A_list.append(next_index)
    new_B_list=B_list.remove(next_index)

    #리스트에 있는 값들이 서로 연결이 되어있나??
    for i in range(len(new_A_list)):
        for j in range(len(G[new_A_list[i]])):
            if new_A_list[i]
def Find_min(N):
    #if조건을 이용해서 종료 조건 확인
    
    A_list.append(N)
    B_list.remove(N)

    length=len(G[N])
    for i in range(length):
        next_index = G[N][i]
        if Promising(next_index)==1:
            A_list.append(next_index)
            B_list.remove(next_index)
            Find_min(next_index)
if __name__ == "__main__":
    N = int(input()) #N개의 구역

    #인구 수 저장.
    population = [] 
    population = list(map(int, input().split()))

    #구역끼리 연결된 정보를 저장.
    G = []
    for i in range(N):
        row_data = list(map(int,input().split()))
        G.append(row_data[1:])
    A_list = []
    B_list = [i for i in range(N)]
    Find_min(0)
'''
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def promising(group, current_node, target_group):
    if group[current_node] != target_group:
        return False
    return True

def bfs(graph, start, visited, group):
    queue = deque([start])
    visited[start] = True
    group[start] = 1  # 시작 노드는 A 선거구에 포함

    while queue:
        current_node = queue.popleft()

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                group[neighbor] = 1 if group[current_node] == 2 else 2

def calculate_population(group, population):
    A_pop = 0
    B_pop = 0

    for i in range(1, N + 1):
        if group[i] == 1:
            A_pop += population[i - 1]
        else:
            B_pop += population[i - 1]

    return abs(A_pop - B_pop)

def is_connected(graph, nodes, group):
    visited = [False] * (N + 1)
    for node in nodes:
        start_node = node
        break

    bfs(graph, start_node, visited, group)

    for node in nodes:
        if not visited[node]:
            return False

    return True

def divide_areas(graph, population):
    min_difference = float('inf')

    for r in range(1, N // 2 + 1):
        for comb in combinations(range(1, N + 1), r):
            A_list = list(comb)
            B_list = [i for i in range(1, N + 1) if i not in A_list]

            if is_connected(graph, A_list, [0] * (N + 1)) and is_connected(graph, B_list, [0] * (N + 1)):
                difference = calculate_population([0] + [1 if i in A_list else 2 for i in range(1, N + 1)], population)
                min_difference = min(min_difference, difference)

    return min_difference if min_difference != float('inf') else -1

if __name__ == "__main__":
    N = int(input())  # N개의 구역

    # 인구 수 저장.
    population = list(map(int, input().split()))

    # 구역끼리 연결된 정보를 저장.
    G = {}
    for i in range(1, N + 1):
        row_data = list(map(int, input().split()))[1:]
        G[i] = row_data

    result = divide_areas(G, population)
    print(result)

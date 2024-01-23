# Baekjoon_2178 Solution
# 미로를 이동시키는 방법은 row - 1, row + 1, col + 1

# 미로를 움직일 수 있는 Promising한 조건
def Promising(m, n):  # m은 col, n은 row
    if 0 <= m < col and 0 <= n < row and G[n][m] == 1 and saved_G[n][m] == 0:
        return True
    return False

# 미로를 가는 최소 count 구하는 backtracking 알고리즘
def Find_count(s_x, s_y):
    global count  # count를 global 변수로 사용
    if s_x == col - 1 and s_y == row - 1:
        print(count)
        return True

    if Promising(s_x, s_y - 1):
        count += 1
        saved_G[s_y - 1][s_x] = 1
        if Find_count(s_x, s_y - 1):
            return True

    if Promising(s_x, s_y + 1):
        count += 1
        saved_G[s_y + 1][s_x] = 1
        if Find_count(s_x, s_y + 1):
            return True

    if Promising(s_x + 1, s_y):
        count += 1
        saved_G[s_y][s_x + 1] = 1
        if Find_count(s_x + 1, s_y):
            return True

    count -= 1
    saved_G[s_y][s_x] = 0
    return False

# 행과 열 입력 받기
row, col = map(int, input().split())
count = 1
G = []
saved_G = [[0 for i in range(col)] for j in range(row)]  # 내가 지나온 길

# 2차원 배열 선언 및 입력 받기
for i in range(row):
    row_data = list(map(int, input().split()))
    G.append(row_data)

if Find_count(0, 0):
    #print("Find minimum count")

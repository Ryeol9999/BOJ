# 색종이

N = int(input())
arr = [[0 for i in range(100)] for j in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] += 1
count = 0
# def dfs(x,y):
#     global  count
#     count += 1
#     arr[x][y] == 0
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx < 100 and 0 <= ny < 100 and arr[nx][ny] != 0:
#             dfs(nx,ny)

for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            count += 1
print(count)
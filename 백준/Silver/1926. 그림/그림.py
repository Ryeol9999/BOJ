from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
max_count = 0
greem = 0
def bfs(x,y):
    global max_count
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    count  = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:

        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]== False and arr[nx][ny] == 1 :
                queue.append((nx,ny))
                visited[nx][ny] = True
                count += 1

    if count > max_count:
        max_count = count
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == False:
            bfs(i,j)
            greem += 1
print(greem)
print(max_count)

N = int(input())
M = int(input())
#dfs
def dfs(idx):
    global visited,count
    visited[idx] = True
    for next in range(1,N+1):
        if not visited[next] and graph[idx][next] == True:
            count +=1
            dfs(next)

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]* (N+1)
count = 0

for _ in range(M):
    a,b =map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(1)
print(count)
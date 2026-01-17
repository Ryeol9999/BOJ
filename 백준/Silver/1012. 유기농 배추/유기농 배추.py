import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    visited[x][y]=True

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False and arr[nx][ny]==1:
            dfs(nx,ny)
            
T= int(input())
for _ in range(T):
    N,M,K= map(int,input().split())
    arr = [[0] * M for _ in range(N)]
    count = 0
    visited =[[False] * M for _ in range(N)]
    for i in range(K):
        a,b= map(int,input().split())
        arr[a][b]=1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                count +=1
    print(count)


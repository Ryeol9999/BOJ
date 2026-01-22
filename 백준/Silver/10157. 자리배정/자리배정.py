import sys

C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

if K > C * R:
    print(0)
    exit()

# 도화지 만들기 (0으로 초기화)
grid = [[0] * R for _ in range(C)]
curr_x, curr_y = 0, 0
way = 1 # 1: 상, 2: 우, 3: 하, 4: 좌
cnt = 1

while cnt < K:
    grid[curr_x][curr_y] = cnt
    
    if way == 1: # 위로 가기 (y 증가)
        if curr_y + 1 < R and grid[curr_x][curr_y + 1] == 0:
            curr_y += 1
            cnt += 1
        else: way = 2 # 막히면 방향 전환
    elif way == 2: # 오른쪽으로 가기 (x 증가)
        if curr_x + 1 < C and grid[curr_x + 1][curr_y] == 0:
            curr_x += 1
            cnt += 1
        else: way = 3
    elif way == 3: # 아래로 가기 (y 감소)
        if curr_y - 1 >= 0 and grid[curr_x][curr_y - 1] == 0:
            curr_y -= 1
            cnt += 1
        else: way = 4
    elif way == 4: # 왼쪽으로 가기 (x 감소)
        if curr_x - 1 >= 0 and grid[curr_x - 1][curr_y] == 0:
            curr_x -= 1
            cnt += 1
        else: way = 1

print(curr_x+1, curr_y+1)
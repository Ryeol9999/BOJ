import sys
from collections import deque

def solve() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    out_lines = []
    for _ in range(q):
        k, v = map(int, input().split())
        visited = [False] * (n + 1)
        visited[v] = True
        dq = deque([v])
        cnt = 0
        while dq:
            cur = dq.popleft()
            for nxt, usado in graph[cur]:
                if not visited[nxt] and usado >= k:
                    visited[nxt] = True
                    cnt += 1
                    dq.append(nxt)
        out_lines.append(str(cnt))
    sys.stdout.write("\n".join(out_lines))


solve()
#카드 2
from collections import deque

N = int(input())
dummy = deque([i for i in range(1,N+1)])
# print(dummy)
while len(dummy)>1 :
    dummy.popleft()
    X = dummy.popleft()
    dummy.append(X)

print(*dummy)
#트리

N=int(input())
Arr = list(map(int,input().split()))

Node = int(input())

Tree = [[] for i in range(N)]
for i in range(N):
    if Arr[i] != -1:
        Tree[Arr[i]].append(i)
li= [ ]
def dfs(Node):
    li.append(Node)
    if Tree[Node] != []:
        for i in range(len(Tree[Node])):
            dfs(Tree[Node][i])
    else:
        return
dfs(Node)
count =0
for i in range(N):
    if Tree[i] == [] and i not in li:
        count += 1
    elif Node in Tree[i] and len(Tree[i]) == 1:
        count += 1

print(count)

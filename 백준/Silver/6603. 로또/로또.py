def dfs():
    global s , li
    if len(s) == 6 :
        print(' '.join(map(str, s)))
        return

    for i in range(len(li)):
        if len(s) == 0:
            s.append(li[i])
            dfs()
            s.pop()
        else:
            if li[i] not in s and li[i] > s[-1] :
                s.append(li[i])
                dfs()
                s.pop()

while 1:
    s = []
    li= list(map(int,input().split()))
    if li[0]==0:
        break
    else:
        A=li.pop(0)
        li.sort()
        dfs()
        print()


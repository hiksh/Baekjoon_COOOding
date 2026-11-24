import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        tmp = list(map(int, input().split()))
        G[tmp[0]-1].append(tmp[1]-1)
        G[tmp[1]-1].append(tmp[0]-1)

    visited = [0 for _ in range(N)]

    def DFS(s,g):
        for v in G[s]:
            if visited[v] == 0:
                visited[v] = -g
                DFS(v,-g)
            else:
                if visited[v] == g:
                    return 0

    SUC = 1
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
        SUC = DFS(i,visited[i])
        if SUC == 0:
            print("NO")
            break
    if SUC == None:
        print("YES")
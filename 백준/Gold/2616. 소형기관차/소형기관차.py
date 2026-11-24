import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
N_Cap = int(input())

dp_lst = [[0,0,0,0] for _ in range(N)]
dp_lst[N_Cap-1][1] = sum(T[:N_Cap])

for i in range(1,4):
    for j in range(N_Cap,N):
        T_buffer = sum(T[j-N_Cap+1:j+1])
        dp_lst[j][i] = max(dp_lst[j-N_Cap][i-1]+T_buffer, dp_lst[j-1][i])

print(dp_lst[-1][-1])
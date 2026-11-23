import sys
input = sys.stdin.readline

N = int(input())
R = list(map(int, input().split()))
P = list(map(int, input().split()))

def solve():
    m = P[0]
    cost = 0

    for i in range(N-1):
        m = min(m, P[i])
        cost += m * R[i]

    return cost

print(solve())
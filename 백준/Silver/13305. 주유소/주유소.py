# import sys
# input = sys.stdin.readline

N = int(input())
R = list(map(int, input().split()))
P = list(map(int, input().split()))

def solve(_P):
    points = [len(_P)-1]
    cost = 0

    i = 0
    m_loc = -1
    while True:
        m = min(_P[:m_loc])
        m_loc = _P.index(m)
        points.append(m_loc)

        cost += P[points[i+1]] * sum(R[points[i+1]:points[i]])
        i += 1

        if m_loc == 0:
            return cost

print(solve(P))
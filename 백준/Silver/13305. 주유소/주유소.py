import sys
input = sys.stdin.readline
import copy

N = int(input())
R = list(map(int, input().split()))
P = list(map(int, input().split()))

def set_point(nodes):
    _P = copy.deepcopy(nodes)
    points = []
    while True:
        if len(_P) == 0:
            break

        m = min(_P)
        m_loc = _P.index(m)
        points.append(m_loc)
        _P = _P[:m_loc]

    points.sort()
    return points

# print(set_point(P))
Oiling = set_point(P)
Oiling.append(len(P)-1)

cost = 0
for i in range(len(Oiling)-1):
    cost += P[Oiling[i]] * sum(R[Oiling[i]:Oiling[i+1]])

print(cost)
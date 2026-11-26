N = int(input())
V = []
for i in range(N):
    V.append(input())

def Encode(v, ret):
    in_1 = 0
    in_0 = 0
    for i in v:
        for j in i:
            if '0' in j:
                in_0 = 1
            if '1' in j:
                in_1 = 1

    if in_1 == 1:
        if in_0 == 1:
            tmp1 = v[:len(v)//2]
            tmp2 = v[len(v)//2:]
            ret = f"({Encode([tmp1[i][0:len(v)//2] for i in range(len(v)//2)], "")}{Encode([tmp1[i][len(v)//2:] for i in range(len(v)//2)], "")}{Encode([tmp2[i][0:len(v)//2] for i in range(len(v)//2)], "")}{Encode([tmp2[i][len(v)//2:] for i in range(len(v)//2)], "")})"
            return ret
        else: # 1 만있음
            return ret + '1'
    else: # 1이 없음 (0만 있음)
        return ret + '0'

print(f"{Encode(V, "")}")
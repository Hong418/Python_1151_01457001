N, D_sq = map(int, input().split())

nodes = []
for i in range(N):
    x, y, z, power = map(int, input().split())
    nodes.append((x, y, z ,power))

interference_set = set()

for i in range(N):
    for j in range(i + 1, N):
        n1 = nodes[i]
        n2 = nodes[j]

        distance = (n1[0] - n2[0])**2 + (n1[1] - n2[1])**2 + (n1[2] - n2[2])**2
        if distance <= D_sq and n1[3] != n2[3]:
            if n1 < n2:
                pair = (n1, n2)
            else:
                pair = (n2, n1)

            interference_set.add(pair)

print(f"Interference Pairs: {len(interference_set)}")

for pair in sorted(interference_set):
    nA = pair[0]
    nB = pair[1]
    print(f"({nA[0]}, {nA[1]}, {nA[2]}, {nA[3]}) <-> ({nB[0]}, {nB[1]}, {nB[2]}, {nB[3]})")
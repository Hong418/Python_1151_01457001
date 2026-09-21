n, m = map(int, input().split())

A_friends = set(map(int, input().split()))
B_friends = set(map(int, input().split()))

intersection = A_friends & B_friends

print(len(intersection))

sort_inter = sorted(intersection)

print(*sort_inter)
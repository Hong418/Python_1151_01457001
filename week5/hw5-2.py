def gcd(a, b):
    while b != 0:
        a, b = b , a % b
    return a

def G(n):
    G=0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            G += gcd(i, j)
    return G

while True:
    n = int(input())
    if n == 0:
        break
    ans = G(n)
    print(ans)
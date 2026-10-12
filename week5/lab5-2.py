def Cola(n):
    ans = n
    empty = n
    while empty >= 3:
        new = empty // 3
        ans += new
        empty = (empty % 3) + new
    if empty == 2:
        ans += 1
    return ans

while True:
    try:
        n = int(input())
        ans = Cola(n)
        print(ans)
    except EOFError:
        break
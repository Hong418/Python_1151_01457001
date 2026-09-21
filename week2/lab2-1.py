n = int(input())
if n <= 0:
    print("Invalid input")
else:
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end = " ")
            num += 1
        print()
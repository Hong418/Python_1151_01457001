n = int(input())

if n <= 1:
    print("Invalid input")

else:
    for i in range(1, n + 1):
        outside = " " * (n - i)

        if i == 1:
            print(outside + "*")
        else:
            inside = " " * (2 * i - 3)
            print(outside + "*" + inside + "*")

    for i in range(n - 1, 0, -1):
        outside = " " * (n - i)

        if i == 1:
            print(outside + "*")
        else:
            inside = " " * (2 * i - 3)
            print(outside + "*" + inside + "*")
def count_carry(num1, num2):
    n1, n2 = num1[::-1], num2[::-1]
    c = 0
    c_count = 0
    max_len = max(len(num1), len(num2))

    for i in range (max_len):
        if i < len(n1):
            d1 = int(n1[i])
        else:
            d1 = 0

        if i < len(n2):
            d2 = int(n2[i])
        else:
            d2 = 0

        if d1 + d2 + c >= 10:
            c = 1
            c_count += 1
        else:
            c = 0   

    return c_count   

while True:
    n = input().split()
    num1, num2 = n[0], n[1]

    if num1 == "0" and num2 == "0":
        break

    ans = count_carry(num1, num2)

    if ans == 0:
        print("No carry operation.")
    elif ans == 1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")
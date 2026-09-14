arr = []

while True:
    try:
        new_num = int(input())
    except EOFError:
        break
    arr.append(new_num)

    j = len(arr) - 1
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    L = len(arr)
    if L % 2 == 1:
        median = arr[L // 2]
    else:
        median = (arr[L // 2 - 1] + arr[L // 2]) // 2

    print(median)
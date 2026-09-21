while True:
    try:
        N = int(input())

        if N == 0:
            break

        while True:
            list_input = input().split()
            if len(list_input) == 0:
                continue
                
            if int(list_input[0]) == 0:
                break

            target_list = list(map(int, list_input))

            stack = []
            current_A = 1
            possible = True

            for target in target_list:
                while current_A <= N and (len(stack) == 0 or stack[-1] != target):
                    stack.append(current_A)
                    current_A += 1

                if len(stack) > 0 and stack[-1] == target:
                    stack.pop()
                else:
                    possible = False
                    break

            if possible:
                print("YES")
            else:
                print("NO")
                
    except EOFError:
        break
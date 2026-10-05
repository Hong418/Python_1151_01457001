def Palindromes(s):
    mirror = {
        'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
        'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V',
        'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S',
        '3': 'E', '5': 'Z', '8': '8'
    }

    is_p = True
    is_m = True
    length = len(s)

    for i in range(length):
        if s[i] != s[length - 1 - i]:
            is_p = False

        s_right = s[length - 1 - i]
        if s_right not in mirror or mirror[s_right] != s[i]:
            is_m = False

    if is_p and is_m:
        print(f"{s} -- is a mirrored palindrome.")
    elif is_p and not is_m:
        print(f"{s} -- is a regular palindrome.")
    elif not is_p and is_m:
        print(f"{s} -- is a mirrored string.")
    else:
        print(f"{s} -- is not a palindrome.")
            
while True:
    try:
        s = input().strip()
        Palindromes(s)
    except EOFError:
        break
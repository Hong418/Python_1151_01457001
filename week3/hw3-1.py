n = int(input())

for i in range(n):
    s = input()

    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_char = ""
    max_freq = 0

    for char, freq in char_count.items():
        if freq > max_freq:
            max_freq = freq
            max_char = char

    print(max_char)
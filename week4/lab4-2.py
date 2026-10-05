def word_count():
    s = input()
    words = s.split()

    freq_dict = {}

    for word in words:
        w = word.lower()

        if w not in freq_dict:
            freq_dict[w] = 1
        else:
            freq_dict[w] += 1

    for k, v in freq_dict.items():
        print(f"{k} {v}")

word_count()
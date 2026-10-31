n = int(input())
scores = []

for i in range(n):
    line = input()

    try:
        data = line.split(',')
        if len(data) != 2 or data[1].strip() == "":
            raise ValueError("Error: invalid data format")

        name, s = data[0], data[1]

        try:
            score = int(s)
        except ValueError:
            raise ValueError("Error: invalid score")

        if score > 100 or score < 0:
            raise ValueError("Error: invalid score")

    except ValueError as e:
        print(e)
    else:
        print("OK")
        scores.append(score)

try:
    average = sum(scores) / len(scores)
except ZeroDivisionError:
    print("No valid scores")
else:
    print(f"Average score: {average:.2f}")
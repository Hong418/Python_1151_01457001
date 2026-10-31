def valid(n):
    try:
        float(n)
    except ValueError:
        raise ValueError("Error: please enter a number")

    try:
        num = int(n)
    except ValueError:
        raise ValueError("Error: please enter an integer")

    if num < 0 or num > 50:
        raise ValueError("Error: number out of range")

    return num

count = 0

try:
    n = input()
    ans = valid(n)
except ValueError as e:
    print(e)
else:
    while True:
        guess_input = input()
        count += 1

        try:
            guess = valid(guess_input)
        except ValueError as e:
            print(e)
        else:
            if(guess < ans):
                print("You are too low!")
            elif guess > ans:
                print("You are too high!")
            else:
                print("You got it!")
                break
finally:
    print(f"You guessed {count} times.")
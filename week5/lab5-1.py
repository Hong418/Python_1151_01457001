def sum_even_numbers(*args):
    total = 0
    for num in args:
        if num % 2 == 0:
            total += num
    return total

while True:
    line = input()
    if line == "END":
        break

    numbers = []
    for x in line.split():
        numbers.append(int(x))

    result = sum_even_numbers(*numbers)
    print(result)
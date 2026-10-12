from functools import wraps

def memoize_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n in cache:
            print(f"Cache hit for {func.__name__}({n})")
            return cache[n]
        else:
            ans = func(n)
            print(f"Computed {func.__name__}({n}) = {ans}")
            cache[n] = ans
            return ans
    return wrapper

@memoize_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    try:
        n = int(input())
        ans = fibonacci(n)
        print(f"Final Result: {ans}")
    except EOFError:
        break
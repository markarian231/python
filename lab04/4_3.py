# 4.3
def factorial(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))


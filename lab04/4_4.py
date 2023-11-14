# 4.4
def fibonacci(n):
    if n < 0:
        raise ValueError("Indeks nie moze byc ujemny")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(7))

import itertools
import random

# (0, 1, 0, 1, ...)
iterator01 = itertools.cycle([0, 1])

# Losowa wartosc z listy
random_iterator = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

# Numery dni tygodnia
days_nmb_iterator = itertools.cycle(range(7))

for _ in range(10):
    print(next(iterator01))

for _ in range(10):
    print(next(random_iterator))

for _ in range(16):
    print(next(days_nmb_iterator))

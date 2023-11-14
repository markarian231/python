# 4.5
def reverse_iter(L, left, right):
    if left < 0 or right >= len(L):
        raise ValueError("Indeksy poza zakresem listy")

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def reverse_rec(L, left, right):
    if left < 0 or right >= len(L):
        raise ValueError("Indeksy poza zakresem listy")

    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_rec(L, left + 1, right - 1)

list1 = [1, 2, 3, 4, 5, 6]
reverse_iter(list1, 1, 4)
print(list1)

list2 = [1, 2, 3, 4, 5, 6]
reverse_rec(list2, 1, 4)
print(list2)



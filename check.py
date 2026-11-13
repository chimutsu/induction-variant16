def f(n):
    return 6**(2*n) + 19**n - 2**(n+1)
m = 17
bad = [n for n in range(1, 101) if f(n) % m != 0]
print("Контрприкладів не знайдено" if not bad else bad)

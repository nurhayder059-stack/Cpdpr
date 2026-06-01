n, m = map(int, input().split())

alcohol1 = 0
volume1 = 0

for _ in range(n):
    a, p = map(int, input().split())
    volume1 += a
    alcohol1 += a * p

alcohol2 = 0
volume2 = 0

for _ in range(m):
    a, p = map(int, input().split())
    volume2 += a
    alcohol2 += a * p

if alcohol1 * volume2 == alcohol2 * volume1:
    print("same")
else:
    print("different")
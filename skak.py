rx, ry = map(int, input().split())
px, py = map(int, input().split())

if rx == px or ry == py:
    print(1)
else:
    print(2)
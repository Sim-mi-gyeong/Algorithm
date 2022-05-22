# 네 번째 점

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    a = x3
elif x2 == x3:
    a = x1
else:
    a = x2
if y1 == y2:
    b = y3
elif y2 == y3:
    b = y1
else:
    b = y2
print(a, b)

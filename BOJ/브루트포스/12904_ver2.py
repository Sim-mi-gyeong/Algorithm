# A와 B

s = input()
t = input()

check = False
while len(s) <= len(t):
    if s != t:
        if t[-1] == "A":
            t = t[:-1]
        elif t[-1] == "B":
            t = t[:-1][::-1]
    else:
        check = True
        break
if check:
    print(1)
else:
    print(0)


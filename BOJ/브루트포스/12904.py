# A와 B - 런타임에러

s = input()
t = input()


def cal(t):
    if len(t) == len(s):
        if t == s:
            return True

    elif t[-1] == "A":
        return cal(t[:-1])

    elif t[-1] == "B":
        return cal(t[:-1][::-1])

    return False


if cal(t):
    print(1)
else:
    print(0)

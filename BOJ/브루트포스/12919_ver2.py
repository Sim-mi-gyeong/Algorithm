# A와 B 2

s = input()
t = input()


def reverseStr(s):
    newString = ""
    for i in s[::-1]:
        newString += i
    return newString


def cal(s):
    if s == t:
        return True
    while True:
        beforeS = s
        next = s + "A"
        if next != t[: len(next) + 1]:
            next = reverseStr(beforeS + "B")
            if next == t:
                break
            elif len(next) != len(t) and next != t[: len(next) + 1]:
                s = next
                continue
            elif len(next) == len(t) and next != t[: len(next) + 1]:
                return False

        else:
            break

    return True


if cal(s):
    print(1)
else:
    print(0)

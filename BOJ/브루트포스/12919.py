# A와 B 2
# 처음과 끝의 문자에 따른 연산(문자열 추가/뒤집기) 케이스 분류

s = input()
t = input()


def cal(t):

    if len(s) == len(t):
        return s == t
    if t[-1] == "A":
        # t = t[:-1]
        if cal(t[:-1]):
            return True
    if t[0] == "B":  # BA 가 남은 상태에서 A로 만들기 위해서는, t[-1] == "A" 가 아닌 t[0] == "B" 조건 수행해야 함
        # t = t[::-1][:-1]
        if cal(t[::-1][:-1]):
            return True


if cal(t):
    print(1)
else:
    print(0)

"""
BAAB
BAABB
"""

import time


def solution(s):

    keyboard = {
        "q": (0, 0),
        "w": (0, 1),
        "e": (0, 2),
        "r": (0, 3),
        "t": (0, 4),
        "y": (0, 5),
        "u": (0, 6),
        "i": (0, 7),
        "o": (0, 8),
        "p": (1, 0),
        "a": (1, 1),
        "s": (1, 2),
        "d": (1, 3),
        "f": (1, 4),
        "g": (1, 5),
        "h": (1, 6),
        "j": (1, 7),
        "k": (1, 8),
        "l": (2, 0),
        "z": (2, 1),
        "x": (2, 2),
        "c": (2, 3),
        "v": (2, 4),
        "b": (2, 5),
        "n": (2, 6),
        "m": (2, 7),
    }

    answer = 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = (
                dp[i][j - 1]
                + abs(keyboard[s[j - 1]][0] - keyboard[s[j]][0])
                + abs(keyboard[s[j - 1]][1] - keyboard[s[j]][1])
            )

    print(dp)

    for i in range(n):
        answer += sum(dp[i])

    return answer


start = time.time()
print(solution("abcc"))
end = time.time()
print("걸린 시간 : ", end - start)
print()

start = time.time()
print(solution("tooth"))
end = time.time()
print("걸린 시간 : ", end - start)
print()

start = time.time()
print(solution("zzz"))
end = time.time()
print("걸린 시간 : ", end - start)
print()

start = time.time()
print(solution("icandoithaha"))
end = time.time()
print("걸린 시간 : ", end - start)

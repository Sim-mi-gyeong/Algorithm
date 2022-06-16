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

    n = len(s)  # 문자열 길이
    end = 0
    answer = 0
    # 투포인터를 통해 연속된 부분 문자열 구하기
    for start in range(n):
        end = start
        while end < n:
            # 부분 문자열
            subStr = s[start : end + 1]
            # print("subStr : ", subStr)
            tmp = 0  # 각 부분 문자열의 거리값 저장
            # 부분 문자열 내에서도 2개씩 -> 3개씩 이어가면서 처리
            i, j = 0, 0
            # 사실 이 부분이 필요없고 바로 while end < n: 안에서 처리를 해도 되는데,,
            while i < len(subStr) - 1:
                while j < len(subStr):
                    # print("subStr[i] : ", subStr[i], " subStr[j] : ", subStr[j])
                    j = i + 1
                    tmpDist = abs(keyboard[subStr[i]][0] - keyboard[subStr[j]][0]) + abs(
                        keyboard[subStr[i]][1] - keyboard[subStr[j]][1]
                    )
                    tmp += tmpDist
                    i += 1
                    j += 1

            answer += tmp
            end += 1

    answer %= 1e9 + 7

    return int(answer)


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


"""
23
걸린 시간 :  6.604194641113281e-05

52
걸린 시간 :  2.002716064453125e-05

0
걸린 시간 :  7.152557373046875e-06
"""


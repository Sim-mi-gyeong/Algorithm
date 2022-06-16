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
        tmpSum = 0  # 각 부분 문자열의 거리값 저장
        while end < n:
            # 부분 문자열
            subStr = s[start : end + 1]
            # print("subStr : ", subStr)

            if len(subStr) > 1:
                # tmp = ~ 가 아닌
                # tmp += ~ 를 해야하는 이유는, 앞서 ab 에서 구한 거리에 c 가 붙으면서 -> ab 거리 + bc 의 거리가 추가되어야 하기 때문
                # 즉, 앞의 문자열 거리까지 구해야했기 때문
                tmpSum += abs(keyboard[subStr[-2]][0] - keyboard[subStr[-1]][0]) + abs(
                    keyboard[subStr[-2]][1] - keyboard[subStr[-1]][1]
                )
            end += 1
            # print("tmpSum : ", tmpSum)

            answer += tmpSum
            # print("answer : ", answer)

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
걸린 시간 :  5.507469177246094e-05

52
걸린 시간 :  1.1920928955078125e-05

0
걸린 시간 :  5.0067901611328125e-06
"""


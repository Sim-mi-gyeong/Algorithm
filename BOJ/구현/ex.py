def solution(s):

    dictionary = dict()
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(10):
        dictionary[i] = alpha[i]

    answer = ""
    # 큰 수가 먼저 나올 수 있음
    ansDic = dict()
    for key, value in dictionary.items():
        if value in s:
            ansDic[s.index(value)] = str(key)
            s = s.replace(value, "", 1)
            print("s : ", s)
        elif str(key) in s:
            ansDic[s.index(str(key))] = str(key)
            s = s.replace(str(key), "")
            print("s : ", s)

    print(ansDic)
    # 딕셔너리를 키 값 기준으로 정렬
    for key, value in sorted(ansDic.items()):
        answer += value

    answer = int(answer)

    return answer




print(solution("eightseven4oneeight"))  # 87418
# print(solution("eightone4seven"))

# print("eightone4seven".index("seven"))

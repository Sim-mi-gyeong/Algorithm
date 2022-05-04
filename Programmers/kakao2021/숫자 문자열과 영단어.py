def solution(s):
    alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, j in enumerate(alphabet):
        s = str(i).join(
            s.split(j)
        )  # j 기준 split -> 리스트 원소로 나눠진 후 j가 원소에 X(list 원소를 구분하는 , 에 해당) -> ,(j)를 key(숫자) 기준으로 문자열 concat

    return int(s)


print(solution("one4seveneight"))


def solution(s):

    dic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for key, value in dic.items():
        s = s.replace(key, str(value))
    return int(s)


print(solution("one4seveneight"))

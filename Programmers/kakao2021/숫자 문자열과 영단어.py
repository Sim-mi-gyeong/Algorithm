def solution(s):
    alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, j in enumerate(alphabet):
        s = str(i).join(s.split(j))

    return int(s)


print(solution("one4seveneight"))

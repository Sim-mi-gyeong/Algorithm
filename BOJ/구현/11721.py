# 열 개씩 끊어 출력하기
s = input()
i = 0
while True:
    print(s[i:i+10])
    i += 10
    if len(s[i:]) < 10:
        print(s[i:])
        break
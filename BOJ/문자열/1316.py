# 그룹 단어 체커

n = int(input())
cnt = n
for _ in range(n):
    s = input()
    for i in range(len(s) - 1):
        # .find() : 괄호 안의 문자/숫자 중복 시 가장 첫번째로 등장한 위치를 수로 표현, 중복 무시
        if s.find(s[i]) > s.find(s[i+1]):   # 뒤에 어떤 단어가 나타났지만, 이미 앞 순서에 위치할 때
            cnt -= 1
            break
print(cnt)

n = int(input())
cnt = 0
for i in range(n):
    s = input()
    for j in range(len(s)):
        if j != len(s) - 1:   # 가장 마지막 단어 앞까지
            if s[j] == s[j+1]:
                pass
            elif s[j] in s[j+1:]:   # 앞에서 나온 단어가, 바로 뒤의 단어와 같지 않고 뒤에서 또 나오면,
                break
        else:   # 마지막 단어까지 통과 시
            cnt += 1
print(cnt)
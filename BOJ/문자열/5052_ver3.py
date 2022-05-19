# 전화번호 목록

t = int(input())
for _ in range(t):
    check = True
    n = int(input())
    dic = dict()
    for _ in range(n):
        dic[input()] = 1  # 각 번호를 딕셔너리 키값을 초기화

    for nums in dic:  # 각 번호를 돌면서
        tmp = ""
        for num in nums:  # 각 번호를 구성하는 번호들을 추가해가면서
            tmp += num
            if tmp in dic and tmp != nums:  # 번호를 추가해가는 자기 자신과는 다르지만, 문자열이 딕셔너리에 존재하면(다른 번호의 일부이면)
                check = False
    if check:
        print("YES")
    else:
        print("NO")

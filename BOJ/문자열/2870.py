# 수학숙제

import re

n = int(input())
ans = []
for _ in range(n):
    s = input()
    # num = re.findall("\d+", s)   # 숫자만 필터링해서 리스트로 변환
    num = re.findall("[0-9]+", s)
    a = list(map(int, num))  # map 으로 int형 변환(0으로 시작하는 경우 0 제거)
    ans.extend(a)  # extend() 는 리스트 끝에 가장 바깥쪽 iterable 의 모든 항목을 넣음 / append(x) 는 x 자체를 원소로 넣음

print("\n".join(map(str, sorted(ans))))  # 오름차순 출력

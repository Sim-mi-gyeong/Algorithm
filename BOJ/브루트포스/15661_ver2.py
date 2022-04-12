# 링크와 스타트

from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
people = [i + 1 for i in range(n)]
ans = 1e9
team = dict()

idx = 0
for i in range(1, n):
    team1 = list(combinations(people, i))
    for j in range(len(team1)):
        idx += 1
        # 리스트, 튜플 형태를 모두 set() 으로 감싸면, 집합 자료형으로
        sub1 = set(team1[j])
        sub2 = set(people) - set(sub1)
        team[idx] = [sub1, sub2]

for key, value in team.items():
    tmp1, tmp2 = value[0], value[1]
    power1, power2 = 0, 0
    # 한 명에 대해서는 어차피 더해지는 능력치가 0
    if len(tmp1) != 1:
        subTmp1 = list(combinations(tmp1, 2))
        for sub in subTmp1:
            power1 += s[sub[0] - 1][sub[1] - 1] + s[sub[1] - 1][sub[0] - 1]
    if len(tmp2) != 1:
        subTmp2 = list(combinations(tmp2, 2))
        for sub in subTmp2:
            power2 += s[sub[0] - 1][sub[1] - 1] + s[sub[1] - 1][sub[0] - 1]

    d = abs(power1 - power2)
    if ans >= d:
        ans = d

    if key == len(team) // 2:
        break
print(ans)

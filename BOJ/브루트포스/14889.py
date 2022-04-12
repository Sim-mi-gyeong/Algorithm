# 스타트와 링크

from itertools import combinations

n = int(input())
people = [i + 1 for i in range(n)]
s = [list(map(int, input().split())) for _ in range(n)]
lst = list(combinations(people, n // 2))
team = dict()
for i in range(len(lst) // 2):
    team[i] = [lst[i], lst[len(lst) - 1 - i]]
ans = 1e9
for key, value in team.items():

    team1, team2 = value[0], value[1]

    power1, power2 = 0, 0
    sub1 = list(combinations(team1, 2))
    sub2 = list(combinations(team2, 2))

    for i in range(len(sub1)):
        tmp1, tmp2 = sub1[i], sub2[i]
        power1 += s[tmp1[0] - 1][tmp1[1] - 1] + s[tmp1[1] - 1][tmp1[0] - 1]
        power2 += s[tmp2[0] - 1][tmp2[1] - 1] + s[tmp2[1] - 1][tmp2[0] - 1]

    powerD = abs(power1 - power2)
    if ans >= powerD:
        ans = powerD

print(ans)

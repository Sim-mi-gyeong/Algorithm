# 링크와 스타트

from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
people = [i + 1 for i in range(n)]
ans = 1e9
team = dict()

for i in range(1, n):
    team1 = list(combinations(people, i))
    team2 = []
    for subTeam1 in team1:
        tmpTeam2 = [j for j in people if j not in subTeam1]
        team2.append(tmpTeam2)

    for k in range(len(team1)):
        team[k] = [team1[k], team2[k]]

    for key, value in team.items():
        t1, t2 = value[0], value[1]
        power1, power2 = 0, 0

        if len(t1) != 1:
            sub1 = list(combinations(t1, 2))
            for sub in sub1:
                power1 += s[sub[0] - 1][sub[1] - 1] + s[sub[1] - 1][sub[0] - 1]

        if len(t2) != 1:
            sub2 = list(combinations(t2, 2))
            for sub in sub2:
                power2 += s[sub[0] - 1][sub[1] - 1] + s[sub[1] - 1][sub[0] - 1]

        powerD = abs(power1 - power2)

        if ans >= powerD:
            ans = powerD

print(ans)

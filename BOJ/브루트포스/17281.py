# ⚾

from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]


def play(playerSeq):
    tmpScore = 0
    thisPlayer = 0
    for tmpInning in inning:
        outCnt = 0
        base1, base2, base3 = 0, 0, 0

        while outCnt < 3:

            if tmpInning[playerSeq[thisPlayer]] == 0:
                outCnt += 1
            elif tmpInning[playerSeq[thisPlayer]] == 1:
                tmpScore += base3
                base1, base2, base3 = 1, base1, base2
            elif tmpInning[playerSeq[thisPlayer]] == 2:
                tmpScore += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif tmpInning[playerSeq[thisPlayer]] == 3:
                tmpScore += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            elif tmpInning[playerSeq[thisPlayer]] == 4:
                tmpScore += 1 + base1 + base2 + base3
                base1, base2, base3 = 0, 0, 0

            thisPlayer = (thisPlayer + 1) % 9

    return tmpScore


maxScore = 0
for seq in permutations(range(1, 9), 8):
    seq = list(seq[:3]) + [0] + list(seq[3:])
    tmpScore = play(seq)
    maxScore = max(maxScore, tmpScore)

print(maxScore)

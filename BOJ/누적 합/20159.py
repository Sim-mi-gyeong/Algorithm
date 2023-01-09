# 동작 그만. 밑장 빼기냐?

n = int(input())
lst = list(map(int, input().split()))


evenNum = [0] * (n // 2 + 1)
oddNum = [0] * (n // 2 + 1)
for i in range(0, n):
    if (i + 1) % 2 != 0:
        oddNum[i // 2 + 1] = oddNum[(i // 2)] + lst[i]
    else:
        evenNum[i // 2 + 1] = evenNum[(i // 2)] + lst[i]

maxVal = 0
score = [0] * (n + 1)
for i in range(1, n + 1):
    idx = i // 2 + 1
    if i % 2 != 0:
        score[i] = oddNum[i // 2] + (evenNum[n // 2 - 1] - evenNum[i // 2]) + lst[n - 1]
    else:
        score[i] = oddNum[i // 2] + (evenNum[n // 2 - 1] - evenNum[i // 2 - 1])

    maxVal = max(maxVal, score[i])

print(maxVal)

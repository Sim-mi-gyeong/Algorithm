# 빗물

h, w = map(int, input().split())
graph = [[0] * w for _ in range(h)]
height = list(map(int, input().split()))

total = 0
for i in range(1, w - 1):
    highestLeft = max(height[:i])
    highestRight = max(height[i + 1 :])

    lowerHeight = min(highestLeft, highestRight)

    if height[i] < lowerHeight:
        total += lowerHeight - height[i]

print(total)

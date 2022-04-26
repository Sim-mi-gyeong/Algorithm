# 상어 초등학교

n = int(input())
graph = [[0] * (n) for _ in range(n)]
student = [[] * (n ** 2 + 1) for _ in range(n ** 2 + 1)]
seq = []  # 순서
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(n ** 2):
    num, a, b, c, d = map(int, input().split())
    seq.append(num)
    student[num].append(a)
    student[num].append(b)
    student[num].append(c)
    student[num].append(d)

for s in seq:
    tmpInfo = []  # 가능한 자리/자리에 대한 like/인접 정보를 담을 정보
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                continue
            else:
                like = 0
                empty = 0
                for k in range(len(dx)):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in student[s]:
                            like += 1
                        if graph[nx][ny] == 0:
                            empty += 1
                tmpInfo.append([i, j, like, empty])  # 자리 위치(x, y), 각 자리에 대한 좋아하는 학생, 빈 자리 정보
    # 내림차순 정렬 시 lambda x: -x[0] -> like, empty 는 내림차순 정렬
    # i, j 는 오름차순 정렬
    tmpInfo = sorted(tmpInfo, key=lambda x: (-x[2], -x[3], x[0], x[1]))

    # 자리 앉히기
    posX, posY = tmpInfo[0][0], tmpInfo[0][1]
    graph[posX][posY] = s

total = 0
for i in range(n):
    for j in range(n):
        s = graph[i][j]
        likeCnt = 0
        for k in range(len(dx)):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in student[s]:
                    likeCnt += 1

        # 각 학생 별로 만족도 ++

        if likeCnt <= 1:
            total += likeCnt
        else:
            total += 10 ** (likeCnt - 1)

print(total)

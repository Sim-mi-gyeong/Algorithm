# 신한 코딩테스트 4번
# 두 QR 코드의 유사도 50 초과 X
# 유사도 = X(동일한 위치의 셀이 같은 개수) / (QR 전체 셀의 개수)
# # 는 검은색 / . 은 흰색

# 각 QR 코드별로 90도씩 회전해서 검사

# 최대한 많은 QR 코드 사용한 경우 선택
# -> 선택한 개수가 같은 경우, QR코드 번호 오름차순 정렬 -> 이어붙인 숫자가 가장 작은 경우 선택

# n은 큐알코드 개수 - 각 큐알코드는 qr[i] 번째


def solution(n, qr):
    answer = []
    # newQR = [[] * n for _ in range(n)]

    graph = [[-100] * (n + 1) for _ in range(n + 1)]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                graph[i][j] = 100

    qrDic = dict()

    for i in range(len(qr)):
        tmpQR = [[] * 6 for _ in range(6)]
        for j in range(6):
            for k in range(6):
                # print(qr[i][j][k], end = ' ')
                tmpQR[j].append(qr[i][j][k])

        #     print()
        # print()
        qrDic[i + 1] = tmpQR

    # print(qrDic)

    y = 36
    # 각 큐알 90도씩 회전해야 함
    maxSim = 0
    for i in range(1, n):  # 2번과 3번 ,,,
        # 여기에 회전하는 경우 추가
        for j in range(i + 1, n + 1):  # 1번과 2번, 1번과 3번, ...
            x = 0  # 각 큐알들끼리 같은 거 개수
            for row in range(6):
                for col in range(6):
                    # 1번 큐알과 2번 큐알이 같은지 확인
                    if qrDic[i][row][col] == qrDic[j][row][col]:
                        x += 1

            simirality = round((x / y) * 100, 1)
            # maxSim = max(maxSim, simirality)
            graph[i][j] = simirality
            # graph[i][j] =  maxSim

    # print(graph)
    tmpList = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] != -100 and int(graph[i][j]) <= 50:
                tmpList.append((i, j))

    # print('tmpList : ', tmpList)
    sList = []
    for tmp in tmpList:
        s = ""
        tmp = sorted(tmp)
        for t in tmp:
            s += str(t)
        sList.append(int(s))

    minS = min(sList)
    answer = [int(i) for i in str(minS)]

    return answer

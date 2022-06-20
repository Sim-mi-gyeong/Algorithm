def solution(music):
    answer = 0
    start = 1

    white = [1, 3, 5, 7, 8, 10, 12]
    black = [2, 4, 6, 9, 11]

    whiteDic = dict()
    for i in white:
        whiteDic[i] = 0
    blackDic = dict()
    for i in black:
        blackDic[i] = 0

    for m in music:
        # 흰 색에서 출발
        if start in whiteDic:
            if m in whiteDic:  # 도착지도 흰 색인 경우
                answer += (max(start, m) - min(start, m)) // 2 + 1
            else:  # 도착지는 검은색인 경우
                answer += (max(start, m) - min(start, m)) // 2 + 1
        # 검은색에서 출발
        elif start in blackDic:
            # 도착지가 흰 색인 경우
            if m in whiteDic:
                answer += (max(start, m) - min(start, m)) // 2 + 1
            # 도착지가 검은색인 경우
            else:
                # 출발지는 7 이하인데, 도착지도 7 이하인 경우
                if start <= 7 and m <= 7:
                    answer += (max(start, m) - min(start, m)) // 2 + 1
                # 출발지는 7 이하인데, 도착지는 8 이상인 경우
                elif start <= 7 and m >= 8:
                    answer += (max(start, m) - min(start, m)) // 2 + 2
                # 출발지는 8 이상인데, 도착지도 8 이상인 경우
                elif start >= 8 and m >= 8:
                    answer += (max(start, m) - min(start, m)) // 2 + 1
                # 출발지는 8 이상인데, 도착지가 7 이하인 경우
                else:
                    answer += (max(start, m) - min(start, m)) // 2 + 2
        start = m

    return answer


print(solution([10, 9, 4, 5, 12]))

print()

print(solution([6, 4, 2, 11]))


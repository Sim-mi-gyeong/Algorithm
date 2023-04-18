def solution(sizes):
    answer = 1e9

    maxWidth, maxHeight = 0, 0
    for width, height in sizes:

        # 각 명함 중 더 긴 변이, 가장 긴 가로 / 세로 길이로 수납할 수 있을 때
        # 명함은 회전해서 담을 수 있으므로 가로, 세로 길이는 중요하지 않다
        if width < height:
            width, height = height, width  # 가로를 더 긴 변으로 처리(즉, 세로가 더 길 경우 -> 회전)

        # 긴 쪽의 길이와 짧은 쪽의 길이를 한 곳에 몰아넣은 다음,
        # 긴 쪽의 길이 중에서 가장 큰 값 * 짧은 쪽의 길이 중에서 가장 큰 값을 계산
        maxWidth = max(maxWidth, width)  # 긴 쪽 길이 중에서 최댓값
        maxHeight = max(maxHeight, height)  # 짧은 쪽 길이 중에서는 최댓값

    answer = maxWidth * maxHeight
    return answer

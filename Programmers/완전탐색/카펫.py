def solution(brown, yellow):
    answer = []

    sumVal = brown + yellow
    for col in range(1, sumVal):  # 가능한 너비, 높이 조합
        if sumVal % col:
            continue
        row = sumVal // col
        y = (col - 2) * (row - 2)
        b = sumVal - y

        if (b == brown and y == yellow) and row <= col:
            answer = [col, row]

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

# 부분 수열의 합 - recur, backtracking
# 0번 ~ (n-1)번 인덱스까지 각 원소의 값을 넣고 -> 해당 값을 더하는 경우와 더하지 않는 경우 나눠서(가지치기)

n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0


def sumCal(i, tmpSum):
    global cnt

    if i >= n:
        return
    tmpSum += lst[i]

    if tmpSum == s:
        cnt += 1

    # 현재 lst[i]를 선택한 경우의 가지
    sumCal(i + 1, tmpSum)
    # 현재 lst[i]를 선택하지 않은 경우의 가지
    sumCal(i + 1, tmpSum - lst[i])


sumCal(0, 0)
print(cnt)

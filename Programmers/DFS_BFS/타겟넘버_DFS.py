ans = 0


def dfs(numbers, target, idx, tmpVal):  # cnt : 몇 번째 수를 더하고/뺄지, tmpVal : 수를 연산한 값
    global ans
    if idx == n and tmpVal == target:  # numbers 의 모든 수를 탐색한 경우
        ans += 1
        return
    elif idx == n:
        return

    dfs(numbers, target, idx + 1, tmpVal + numbers[idx])
    dfs(numbers, target, idx + 1, tmpVal - numbers[idx])


def solution(numbers, target):
    global n
    answer = 0
    n = len(numbers)

    dfs(numbers, target, 0, 0)
    answer = ans
    return answer

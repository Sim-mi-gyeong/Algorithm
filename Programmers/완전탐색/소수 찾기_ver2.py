import math


def prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    n = len(numbers)
    check = [0] * n  # numbers 의 각 숫자 사용 여부
    result = set()

    def dfs(number):
        if len(number) == i:  # 1, 2, .. , n 개의 숫자씩 result 추가
            result.add(int(number))
            return

        for j in range(n):  # numbers 의 각 숫자 중 사용여부를 확인하며 조합 생성
            if check[j]:
                continue
            else:
                check[j] = 1
                dfs(number + numbers[j])
                check[j] = 0

    for i in range(1, n + 1):
        dfs("")

    for num in result:
        if prime(num):
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))

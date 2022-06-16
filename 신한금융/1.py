import re


def solution(accounts):
    answer = 0

    # accounts 내의 문자열 중 올바른 계좌번호 개수 리턴
    for account in accounts:
        if account.isdigit():
            if 12 <= len(account) <= 14:
                answer += 1
            elif bool(re.search("^010", account)) and len(account) == 11:
                answer += 1
    return answer


print(solution(["01012345678", "Th1s1sAccountNumber", "9876543210123", "2208875699"]))

print(solution(["InvalidAccountNumber"]))


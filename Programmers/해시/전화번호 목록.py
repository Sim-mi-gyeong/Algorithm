def solution(phone_book):
    answer = True
    # 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치
    phone_book = sorted(phone_book)

    # 1번 풀이
    for i in range(len(phone_book[:-1])):
        # if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break

    # 2번 풀이
    # for num1, num2 in zip(phone_book, phone_book[1:]):
    #     if num2.startswith(num1):
    #         answer = False
    #         return answer

    # 3번 풀이
    # dic = dict()
    # for i in phone_book:
    #     dic[i] = 1
    # for num in phone_book:
    #     tmp = ""
    #     for j in num:
    #         tmp += j
    #         if tmp in dic and tmp != num:
    #             answer = False

    return answer


print(solution(["119", "97674223", "1195524421"]))

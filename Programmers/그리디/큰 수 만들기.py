def solution(number, k):

    max = 0
    string_list = [i for i in number]
    string = ''
    sub = 0
    # for i in range(k):
    #     for j in range(len(number)):
    #         string.replace(number[j], '')
    #         if int_string < int(string):
    #             int_string = int(string)
    i = 0
    j = i + 1
    while(sub != k):
        string_list = [a for a in number]
        string_list.remove(number[i])
        print(string_list)
        sub += 1
            
        string_list.remove(number[j])
        print(string_list)
        sub += 1
        for a in string_list:
            string += a
        if max < int(string):
            max = int(string)
        # string = number   # 문자열 초기화
        j += 1
        if j == len(number) - 1:
            i += 1
            j = i + 1
        if i >= len(number) - k + 1:
            break
    answer = str(max)     
    return answer

n = input()
k = int(input())
print(solution(n, k))
print(type(solution(n, k)))


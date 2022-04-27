# 백만 장자 프로젝트

t = int(input())
for _ in range(t):
    n = int(input())  # 매매가 개수
    lst = list(map(int, input().split()))  # 매매가 정보
    lst = lst[::-1]
    # 뒤에서부터 시작해서(거꾸로 뒤집어서) 만약, i 번째가 i-1 번째보다 크다면(팔아서 이익을 얻을 수 있다면)
    # 사고 팔기

    # 9 5 3
    # 2 1 3 1 1
    buy = 0
    sell = 0
    benefit = 0
    for i in range(len(lst) - 1):
        # buy = 0
        # sell = 0
        print("i 가 ", i, " 일 때")
        j = i + 1
        maxVal = 0
        # 9 5 3  중에서는 3 에 살 때, 5 와 9 중 큰 값에 팔도록 해야 함 -> 즉, 9에 대해 5와 3 중 차이가 더 큰 것만 저장해서 benefit에
        while lst[i] > lst[j]:
            if lst[i] < lst[j]:
                break
            # maxVal = max(maxVal, lst[i] - lst[j])
            benefit += lst[i] - lst[j]
            print("benefit : ", benefit)
            j += 1
            if j >= len(lst):
                break
            # if lst[i] < lst[j]:
            #     break
        # benefit += maxVal

    #     for j in range(i + 1, len(lst)):
    #         print("j 가 ", j, " 일 때")
    #         if lst[i] > lst[j]:
    #             pass
    #         elif lst[i] > lst[j]:
    #             buy += lst[j]
    #         if lst[j] < lst[j - 1]:
    #             sell += lst[i] - buy
    #             print("sell : ", sell)
    #             # buy = 0
    #             continue
    # print("sell : ", sell)
    print("benefit : ", benefit)

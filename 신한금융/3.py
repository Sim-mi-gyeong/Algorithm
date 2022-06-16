import heapq


def solution(n, recipes, orders):
    answer = 0

    cnt = 0

    dic = dict()
    n = len(orders)
    maxTime = 0

    for recipe in recipes:
        recipe = recipe.split(" ")
        name, time = recipe[0], int(recipe[1])
        maxTime = max(maxTime, time)
        if name not in dic:
            dic[name] = time

    print("maxTime : ", maxTime)

    resultDic = dict()
    ans = 0
    # start, end 범위를 통해 이진탐색 수행
    start = 0
    end = maxTime * len(orders)  # max 소요시간은 (가장 오래 걸리는 요리의 요리 시간 * 요리 개수)

    while start <= end:
        mid = (start + end) // 2
        print("mid : ", mid)
        process = 0
        capa = 0
        for order in orders:
            order = order.split(" ")
            menu, orderTime = order[0], int(order[1])
            process += dic[menu]
            # capa += (mid // process)

        capa = mid // process
        print("capa : ", capa)

        if capa >= n:
            end = mid - 1
            print("mid, process, capa : ", mid, process, capa)

            if mid > ans:
                ans = mid
        else:
            start = mid + 1

    print("ans : ", ans)
    answer = int(orders[-1].split(" ")[1]) + ans

    return answer


print(solution(2, ["A 3", "B 2"], ["A 1", "A 2", "B 3", "B 4"]))

print()

print(
    solution(
        3,
        ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"],
        ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "PIZZA 7", "SPAGHETTI 8"],
    )
)

print()

print(solution(1, ["COOKIE 10000"], ["COOKIE 300000"]))

